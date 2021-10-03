from tabulate import tabulate

class Launareiknir:

    def __init__(self, dagvinna, vakta_alag_33_timar, vakta_alag_55_timar):
        self.dagvinnu_timar = dagvinna + 10 
        self.neysluhle = dagvinna + 10 
        self.vetrarorlof = dagvinna + 10
        self.vakta_alag_33_timar = vakta_alag_33_timar
        self.vakta_alag_55_timar = vakta_alag_55_timar + 10
        self.dagvinna_taxti = 2256.09
        self.vakta_alag_33_taxti = 744.51
        self.vakta_alag_55_taxti = 1240.85
        self.neysluhle_taxti = 335.82
        self.vetrarorlof_taxti = 104.91
        self.dagvinna_upphaed = 0
        self.vakta_alag_33_upphaed = 0
        self.vakta_alag_55_upphaed = 0
        self.neysluhle_upphaed = 0
        self.vetrarorlof_upphaed = 0
        # self.vakta_alag_90_taxti = 2030.48
        # self.yfirvinna_taxti = 4029.87
        # self.storhatidarkaup_taxti = 5335.65
        self.orlofsreiknir = 0.1017 # 10.17%
        self.idgjaldsreiknir = 0.04 # 4%
        self.felagsgjaldsreiknir = 0.007 # 0.70%
        self.laun = 0 # Laun fyrir allan frádrátt / Staðgreiðsluskyld laun
        self.fradrattur = 0 # Allur frádráttur samtals
        self.utborgud_laun = 0 # Laun - frádráttur = útborguð laun
        self.orlof = 0 # 10.17% af launum, vetrarorlof ekki tekið með samt
        self.lifeyrissjodur = 0 # Iðgjald 4% + Iðgjald 4% Séreign
        self.felagsgjald = 0
        self.personuafslattur = 50792
        self.stadgreidslustofn = 0 # Laun - lífeyrissjóður (iðgjöldin)
        self.stadgreidsla_threp1 = 0
        self.stadgreidsla_threp2 = 0
        self.stadgreidsla_fyrir_skatt = 0
        self.stadgreidsla_eftir_skatt = 0
        self.threp1 = 0.3145
        self.threp2 = 0.3795
        self.threp2flag = False
        self.threp1_max = 349018
        self.threp2_min = 349019
        self.threp2_max = 979847
        # self.threp3 = 0.4625 # Þetta er bara fyrir crazy rich fólk
        self.reikna()

    def reikna(self):
        self.dagvinna_upphaed = self.dagvinnu_timar * self.dagvinna_taxti
        self.vakta_alag_33_upphaed = self.vakta_alag_33_timar * self.vakta_alag_33_taxti
        self.vakta_alag_55_upphaed = self.vakta_alag_55_timar * self.vakta_alag_55_taxti
        self.neysluhle_upphaed = self.neysluhle * self.neysluhle_taxti
        self.vetrarorlof_upphaed = self.vetrarorlof * self.vetrarorlof_taxti
        self.reikna_laun()
        self.lifeyrissjodur = (self.idgjaldsreiknir * self.laun) * 2
        self.felagsgjald = self.felagsgjaldsreiknir * self.laun
        self.stadgreidslustofn = self.laun - self.lifeyrissjodur
        self.reikna_fradratt()
        self.utborgud_laun = self.laun - self.fradrattur

    def reikna_laun(self):
        self.laun += self.dagvinna_upphaed
        self.laun += self.vakta_alag_33_upphaed
        self.laun += self.vakta_alag_55_upphaed
        self.laun += self.neysluhle * self.neysluhle_taxti
        self.orlof = self.orlofsreiknir * self.laun
        self.laun += self.vetrarorlof * self.vetrarorlof_taxti
        self.laun += self.orlof

    def reikna_fradratt(self):
        threp2_upphaed = 0
        if self.laun <= self.threp1_max and self.laun >= 0:
            self.stadgreidsla_threp1 = self.stadgreidslustofn * self.threp1
        elif self.laun >= self.threp2_min and self.laun < self.threp2_max:
            self.threp2flag = True
            self.stadgreidsla_threp1 = self.threp1_max * self.threp1
            threp2_upphaed = self.stadgreidslustofn - self.threp1_max
            self.stadgreidsla_threp2 = threp2_upphaed * self.threp2

        self.stadgreidsla_fyrir_skatt = self.stadgreidsla_threp1 + self.stadgreidsla_threp2
        self.stadgreidsla_eftir_skatt = self.stadgreidsla_fyrir_skatt - self.personuafslattur
        self.fradrattur = self.orlof + self.lifeyrissjodur + self.felagsgjald + self.stadgreidsla_eftir_skatt

    def prenta_upplysingar_um_tima(self):
        print()
        print(tabulate([
            ["Dagvinna", self.dagvinnu_timar, self.dagvinna_taxti, f"{self.dagvinna_upphaed:,.0f}kr"],
            ["Vaktaálag 33%", self.vakta_alag_33_timar, self.vakta_alag_33_taxti, f"{self.vakta_alag_33_upphaed:,.0f}kr"],
            ["Vaktaálag 55%", self.vakta_alag_55_timar, self.vakta_alag_55_taxti, f"{self.vakta_alag_55_upphaed:,.0f}kr"],
            ["Neysluhlé", self.neysluhle, self.neysluhle_taxti, f"{self.neysluhle_upphaed:,.0f}kr"],
            ["Vetrarorlof", self.vetrarorlof, self.vetrarorlof_taxti, f"{self.vetrarorlof_upphaed:,.0f}kr"],
            ["Orlof 10.17%", None, None, f"{self.orlof:,.0f}kr"],
            ["Samtals laun", None, None, f"{self.laun:,.0f}kr"]

        ], headers=["Laun", "Tímar", "Taxti", "Upphæð"], tablefmt="psql", numalign="center", floatfmt=(".0f", ".0f", ".2f", ".0f")))

    def prenta_upplysingar_um_skattathrep(self):
        print(tabulate([
            ["Staðgreiðsluskyld laun", f"{self.laun:,.0f}kr"],
            ["Lífeyrissjóðir", f"{self.lifeyrissjodur:,.0f}kr"],
            ["Staðgreiðslustofn", f"{self.stadgreidslustofn:,.0f}kr"],
        ], tablefmt="psql", numalign="right", floatfmt=(".0f", ".0f")))
        if not self.threp2flag:
            print(tabulate([
                ["Þrep 1", f"{self.threp1_max:,.0f}kr", "31,45%", f"{self.stadgreidsla_threp1:,.0f}kr"],
            ], tablefmt="psql", numalign="right"))
        else:
            print(tabulate([
                ["Þrep 1", f"{self.threp1_max:,.0f}kr", "31,45%", f"{self.stadgreidsla_threp1:,.0f}kr"],
                ["Þrep 2", f"{self.stadgreidslustofn-self.threp1_max:,.0f}kr", "37,95%", f"{self.stadgreidsla_threp2:,.0f}kr"]
            ], tablefmt="psql", numalign="right"))

    def prenta_upplysingar_um_fradratt(self):
        print(tabulate([
            ["Orlof lagt í banka", f"{self.orlof:,.0f}kr"],
            ["Iðgjald 4%", f"{self.lifeyrissjodur/2:,.0f}kr"],
            ["Iðgjald séreign 4%", f"{self.lifeyrissjodur/2:,.0f}kr"],
            ["Félagsgjald 0.70%", f"{self.felagsgjald:,.0f}kr"],
            ["Staðgreiðsla skatta", f"{self.stadgreidsla_eftir_skatt:,.0f}kr"],
            ["Samtals frádráttur", f"{self.fradrattur:,.0f}kr"]

        ], headers=["Frádráttur", "Upphæð"], tablefmt="psql", numalign="right", floatfmt=(".0f", ".0f")))

    def prenta_upplysingar_um_laun(self):
        print(tabulate([
            ["Laun", f"{self.laun:,.0f}kr"],
            ["Frádráttur", f"{self.fradrattur:,.0f}kr"],
            ["Útborguð laun", f"{self.utborgud_laun:,.0f}kr"],
        ], tablefmt="psql", numalign="right", floatfmt=(".0f", ".0f")))

    def __str__(self):
        return f"Laun: {self.laun:,.0f} kr\nFrádráttur: {self.fradrattur:,.0f}\nÚtborguð laun: {self.utborgud_laun:,.0f}\n"


def main():
    laun = Launareiknir(96, 8, 88)
    laun.prenta_upplysingar_um_tima()
    laun.prenta_upplysingar_um_fradratt()
    laun.prenta_upplysingar_um_skattathrep()
    laun.prenta_upplysingar_um_laun()

if __name__ == "__main__":
    main()

