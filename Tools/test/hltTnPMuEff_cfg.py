import FWCore.ParameterSet.Config as cms

process = cms.Process("EFFICIENCY")

process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring(

        # Z 710pre9 RelVal
        '/store/relval/CMSSW_7_1_0_pre9/RelValZMM_13/GEN-SIM-RECO/POSTLS171_V11-v1/00000/3C9692C5-6DF0-E311-BA9A-002618943935.root',
        '/store/relval/CMSSW_7_1_0_pre9/RelValZMM_13/GEN-SIM-RECO/POSTLS171_V11-v1/00000/F03E1E20-76F0-E311-977D-003048678DA2.root',

        ),
                            secondaryFileNames = cms.untracked.vstring()
                            )

process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
process.GlobalTag.globaltag = "POSTLS171_V11::All"

process.load("Configuration.StandardSequences.MagneticField_38T_cff")
process.load("Configuration.Geometry.GeometryIdeal_cff")
process.load("Geometry.CommonDetUnit.globalTrackingGeometry_cfi")
process.load("RecoMuon.DetLayers.muonDetLayerGeometry_cfi")
process.load("TrackPropagation.SteppingHelixPropagator.SteppingHelixPropagatorAny_cfi")

# # HLT_IsoMu24 = hltL1sMu16, hltL2fL1sMu16L1f0L2Filtered16Q, hltL3fL1sMu16L1f0L2f16QL3Filtered24Q, hltL3crIsoL1sMu16L1f0L2f16QL3f24QL3crIsoRhoFiltered0p15
# TRIGNAME = "IsoMu24"
# PROBEDEN = [ "",     "",           "hltL1sMu16",                     "hltL2fL1sMu16L1f0L2Filtered16Q",       "hltL3fL1sMu16L1f0L2f16QL3Filtered24Q"                    ] 
# PROBENUM = [ "",     "hltL1sMu16", "hltL2fL1sMu16L1f0L2Filtered16Q", "hltL3fL1sMu16L1f0L2f16QL3Filtered24Q", "hltL3crIsoL1sMu16L1f0L2f16QL3f24QL3crIsoRhoFiltered0p15" ] 
# NAMEPLOT = [ "Full", "L1",         "L2overL1",                       "L3overL2",                             "ISOoverL3"                                               ] 

# HLT_M40 = hltL1sMu16, hltL2fL1sMu16L1f0L2Filtered16Q, hltL3fL1sMu16L1f0L2f16QL3Filtered40Q 
TRIGNAME = "Mu40"
PROBEDEN = [ "",     "",           "hltL1sMu16",                     "hltL2fL1sMu16L1f0L2Filtered16Q"       ] 
PROBENUM = [ "",     "hltL1sMu16", "hltL2fL1sMu16L1f0L2Filtered16Q", "hltL3fL1sMu16L1f0L2f16QL3Filtered40Q" ] 
NAMEPLOT = [ "Full", "L1",         "L2overL1",                       "L3overL2"                             ] 

#process.schedule = cms.Schedule()

for i in range(len(PROBEDEN)):
    PROCMODU = TRIGNAME+NAMEPLOT[i]
    PROCPATH = 'Path'+PROCMODU
    module =cms.EDAnalyzer("MuonTriggerEfficiencyAnalyzer",
                           vertexes = cms.InputTag("offlinePrimaryVertices"),
                           muons = cms.InputTag("muons"),
                           triggerProcess = cms.string("HLT"), #"TEST"
                           tagTriggerName = cms.string("HLT_IsoMu24_v"),
                           triggerName = cms.string("HLT_"+TRIGNAME+"_v"), 
                           probeFilterDen = cms.string(PROBEDEN[i]),
                           probeFilterNum = cms.string(PROBENUM[i]),
                           maxNumberMuons = cms.untracked.uint32(999999)
                           )
    setattr(process, PROCMODU, module)
    setattr(process, PROCPATH, cms.Path(module))

#OUTFILE = 'efficiency_'+TRIGNAME
#if PROBENUM != '': OUTFILE = OUTFILE+'_'+PROBENUM
#else:              OUTFILE = OUTFILE+'_fullpath'
#if PROBEDEN != '': OUTFILE = OUTFILE+'_over_'+PROBEDEN
#OUTFILE = OUTFILE+'.root'
#print "Output file: "+OUTFILE

process.TFileService = cms.Service("TFileService",
                                   fileName = cms.string("efficiencies_"+TRIGNAME+'.root'),
                                   closeFileFast = cms.untracked.bool(False)
                                   )


process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(-1))
