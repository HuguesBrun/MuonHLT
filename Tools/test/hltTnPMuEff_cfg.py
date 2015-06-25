import FWCore.ParameterSet.Config as cms

process = cms.Process("EFFICIENCY")

from MuonHLT.Tools.paths_cff import *

# Configuration parameters ##########

pathToStudy = Mu20
tagTriggerName = "HLT_IsoMu24_eta2p1_v"
globalTag = "MCRUN2_74_V9"

fileNames = cms.untracked.vstring(# Z 741 RelVal
    '/store/relval/CMSSW_7_4_1/RelValZMM_13/GEN-SIM-RECO/MCRUN2_74_V9_gensim71X-v1/00000/3682F137-B9EC-E411-8D42-002618943876.root',
    '/store/relval/CMSSW_7_4_1/RelValZMM_13/GEN-SIM-RECO/MCRUN2_74_V9_gensim71X-v1/00000/3AC1823B-B9EC-E411-9DB9-002618943970.root',
    '/store/relval/CMSSW_7_4_1/RelValZMM_13/GEN-SIM-RECO/MCRUN2_74_V9_gensim71X-v1/00000/3EE87BD3-B1EC-E411-B1FC-00261894390B.root',
)
secondaryFileNames = cms.untracked.vstring()

#####################################

process.source = cms.Source("PoolSource",
                            fileNames = fileNames,
                            secondaryFileNames = secondaryFileNames
                            )

process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_PostLS1_cff')
process.load("RecoMuon.DetLayers.muonDetLayerGeometry_cfi")
process.load("TrackPropagation.SteppingHelixPropagator.SteppingHelixPropagatorAny_cfi")

process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')
process.GlobalTag.globaltag = globalTag

#process.schedule = cms.Schedule()

for i in range(len(pathToStudy.PROBEDEN)):
    PROCMODU = pathToStudy.TRIGNAME+pathToStudy.NAMEPLOT[i]
    PROCPATH = 'Path'+PROCMODU
    module =cms.EDAnalyzer("MuonTriggerEfficiencyAnalyzer",
                           vertexes = cms.InputTag("offlinePrimaryVertices"),
                           muons = cms.InputTag("muons"),
                           triggerProcess = cms.string("HLT"), #"TEST"
                           tagTriggerName = cms.string(tagTriggerName),
                           triggerName = cms.string("HLT_"+pathToStudy.TRIGNAME+"_v"), 
                           probeFilterDen = cms.string(pathToStudy.PROBEDEN[i]),
                           probeFilterNum = cms.string(pathToStudy.PROBENUM[i]),
                           maxNumberMuons = cms.untracked.uint32(999999)
                           )
    setattr(process, PROCMODU, module)
    setattr(process, PROCPATH, cms.Path(module))

    process.TFileService = cms.Service("TFileService",
                                   fileName = cms.string("efficiencies_"+pathToStudy.TRIGNAME+'.root'),
                                   closeFileFast = cms.untracked.bool(False)
                                   )


process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(-1))

# Automatic addition of the customisation function from SLHCUpgradeSimulations.Configuration.postLS1Customs
from SLHCUpgradeSimulations.Configuration.postLS1Customs import customisePostLS1 

#call to customisation function customisePostLS1 imported from SLHCUpgradeSimulations.Configuration.postLS1Customs
process = customisePostLS1(process)
