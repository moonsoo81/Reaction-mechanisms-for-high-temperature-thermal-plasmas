# Data sources
database(
    thermoLibraries = ['USC-Mech-ii-revised','primaryThermoLibrary'],
    #reactionLibraries = ['GRI-Mech3.0','ERC-FoundationFuelv0.9','combustion_core/version5','Glarborg/highP','FFCM1(-)'],
    reactionLibraries = ['GRI-Mech3.0','ERC-FoundationFuelv0.9','combustion_core/version5'],
    seedMechanisms = [],
    kineticsDepositories = 'default', 
    kineticsFamilies = 'default',
    kineticsEstimator = 'rate rules',
)


# List of species
species(
    label='C2H6',
    reactive=True,
    structure=SMILES("CC"),
)

species(
    label='CO2',
    reactive=True,
    structure=SMILES("O=C=O"),
)


species(
    label='Ar',
    reactive=False,
    structure=SMILES("[Ar]"),
)

# Reaction systems
simpleReactor(
    temperature=(1500,'K'),
    pressure=(1.0,'bar'),
    initialMoleFractions={
        "C2H6": 0.09,
        "CO2": 0.21,
        "Ar" : 0.7
    },
    terminationConversion={
        'C2H6': 0.99,
    },
    terminationTime=(1e6,'s'),
)

simpleReactor(
    temperature=(2500,'K'),
    pressure=(1.0,'bar'),
    initialMoleFractions={
        "C2H6": 0.09,
        "CO2": 0.21,
        "Ar" : 0.7
    },
    terminationConversion={
        'C2H6': 0.99,
    },
    terminationTime=(1e6,'s'),
)

simpleReactor(
    temperature=(3500,'K'),
    pressure=(1.0,'bar'),
    initialMoleFractions={
        "C2H6": 0.09,
        "CO2": 0.21,
        "Ar" : 0.7
    },
    terminationConversion={
        'C2H6': 0.99,
    },
    terminationTime=(1e6,'s'),
)


simpleReactor(
    temperature=(4500,'K'),
    pressure=(1.0,'bar'),
    initialMoleFractions={
        "C2H6": 0.09,
        "CO2": 0.21,
        "Ar" : 0.7
    },
    terminationConversion={
        'C2H6': 0.99,
    },
    terminationTime=(1e6,'s'),
)



simulator(
    atol=1e-16,
    rtol=1e-8,
)

model(
    toleranceKeepInEdge=0,
    toleranceMoveToCore=0.02,
    toleranceInterruptSimulation=0.5,
    maximumEdgeSpecies=100000
)

# optional block adds constraints on what RMG can output.
# This is helpful for improving the efficiency of RMG, but wrong inputs can lead to many errors.
generatedSpeciesConstraints(
    # allows exceptions to the following restrictions
    allowed=['input species', 'seed mechanisms', 'reaction libraries'],
    maximumCarbonAtoms=3,
    maximumRadicalElectrons=2,
)


pressureDependence(
    method='modified strong collision',
    maximumGrainSize=(0.5,'kcal/mol'),
    minimumNumberOfGrains=250,
    temperatures=(300,5000,'K',8),
    pressures=(0.01,100,'bar',5),
    interpolation=('Chebyshev', 6, 4),
)



options(
    units='si',
    generateOutputHTML=False,
    generatePlots=False,
)
