# -*- coding: utf-8 -*-
"""
Created on Tue May  6 08:09:58 2014

@author: Johan Zietsman, Christoff Kok
"""
__version__ = "0.2.0"

import os
import unittest

from auxi.core.object_test import TestAllFunctions as object_test_all
from auxi.core.namedobject_test import TestAllFunctions as namedobject_test_all

from auxi.tools.chemistry.stoichiometry_test import TestAllFunctions as stoich_test_all
from auxi.tools.chemistry.thermochemistry_test import TestAllFunctions as thermo_test_all

from auxi.modeling.financial.des.transactiontemplate_test import TestAllFunctions as transactiontemplate_test_all
from auxi.modeling.financial.des.transaction_test import TestAllFunctions as transaction_test_all
from auxi.modeling.financial.des.generalledgeraccount_test import TestAllFunctions as generalledgeraccount_test_all
from auxi.modeling.financial.des.generalledgerstructure_test import TestAllFunctions as generalledgerstructure_test_all
from auxi.modeling.financial.des.generalledger_test import TestAllFunctions as generalledger_test_all

from auxi.modeling.process.materials.chemistry.material_test import TestMaterial as chem_test_material
from auxi.modeling.process.materials.chemistry.material_test import TestMaterialPackage as chem_test_material_package
from auxi.modeling.process.materials.thermochemistry.material_test import TestMaterial as thermo_test_material
from auxi.modeling.process.materials.thermochemistry.material_test import TestMaterialPackage as thermo_test_material_package
from auxi.modeling.process.materials.psd.material_test import TestMaterial as psd_test_material
from auxi.modeling.process.materials.psd.material_test import TestMaterialPackage as psd_test_material_package


def run_all():
    # os.system("cls")
    print(__name__)
    unittest.main(module=__name__)
