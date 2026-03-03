# Data sources
database(
    thermoLibraries = ['NOx_Thermo','primaryThermoLibrary'],
    reactionLibraries = ['CPark_NOx_Mech','GRI-Mech3.0-N','NOx2018'],
    seedMechanisms = [],
    kineticsDepositories = 'default', 
    kineticsFamilies = 'default',
    kineticsEstimator = 'rate rules',
)


# List of species
species(
    label='N2',
    reactive=True,
    structure=SMILES("N#N"),
)

species(
    label='O2',
    reactive=True,
    structure=SMILES("[O][O]"),
)

species(
    label='NO',
    reactive=True,
    structure=SMILES("[N]=O"),
)

species(
    label='NO2',
    reactive=True,
    structure=SMILES("[O]N=O"),
)

species(
    label='Ar',
    reactive=False,
    structure=SMILES("[Ar]"),
)

# Reaction systems

simpleReactor(
    temperature=(4999,'K'),
    pressure=(1.0,'bar'),
    initialMoleFractions={
        "N2": 0.05,
        "O2": 0.05,
		"Ar": 0.9,
    },
    terminationConversion={
        'O2': 0.9,
    },
    terminationTime=(10,'s'),
)

simpleReactor(
    temperature=(4000,'K'),
    pressure=(1.0,'bar'),
    initialMoleFractions={
        "N2": 0.05,
        "O2": 0.05,
		"Ar": 0.9,
    },
    terminationConversion={
        'O2': 0.9,
    },
    terminationTime=(10,'s'),
)


simpleReactor(
    temperature=(3000,'K'),
    pressure=(1.0,'bar'),
    initialMoleFractions={
        "N2": 0.05,
        "O2": 0.05,
		"Ar": 0.9,
    },
    terminationConversion={
        'O2': 0.9,
    },
    terminationTime=(10,'s'),
)


simpleReactor(
    temperature=(2000,'K'),
    pressure=(1.0,'bar'),
    initialMoleFractions={
        "N2": 0.05,
        "O2": 0.05,
		"Ar": 0.9,
    },
    terminationConversion={
        'O2': 0.9,
    },
    terminationTime=(10,'s'),
)

simulator(
    atol=1e-16,
    rtol=1e-8,
)

model(
    toleranceKeepInEdge=0.005,
    toleranceMoveToCore=0.05,
    toleranceInterruptSimulation=0.5,
    maximumEdgeSpecies=100000,
    filterReactions=True
)

pressureDependence(
    method='modified strong collision',
    maximumGrainSize=(0.5, 'kcal/mol'),
    minimumNumberOfGrains=250,
    temperatures=(300, 5000, 'K', 8),
    pressures=(0.01, 10, 'bar', 5),
    interpolation=('Chebyshev', 6, 4),
    #maximumAtoms=15,
)

# optional block adds constraints on what RMG can output.
# This is helpful for improving the efficiency of RMG, but wrong inputs can lead to many errors.
generatedSpeciesConstraints(
    # allows exceptions to the following restrictions
    allowed=['input species', 'seed mechanisms', 'reaction libraries'],
    maximumNitrogenAtoms=2,
    maximumOxygenAtoms=2,
    maximumRadicalElectrons=3,
)


options(
    units='si',
    generateOutputHTML=False,
    generatePlots=False,
)
