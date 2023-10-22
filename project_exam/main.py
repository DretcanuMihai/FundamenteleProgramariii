#modul ce construieste si ruleaza aplicatia

from Domeniu.Validatoare.ValidatorMelodie import ValidatorMelodie
from Infrastructura.Repozitorii.RepozitoriuMelodii import RepozitoriuMelodii
from Servicii.ServiciuMelodii import ServiciuMelodii
from UI.UI_Melodii import UI_Melodii

if __name__=="__main__":
    validator_melodie=ValidatorMelodie()
    repozitoriu_melodii=RepozitoriuMelodii("melodii.txt")
    serviciu_melodii=ServiciuMelodii(repozitoriu_melodii,validator_melodie)
    ui_melodii=UI_Melodii(serviciu_melodii)
    ui_melodii.ruleaza()

