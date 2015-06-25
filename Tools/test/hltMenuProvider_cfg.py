import FWCore.ParameterSet.Config as cms

process = cms.Process("HLTMENU")

process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring(
    '/store/relval/CMSSW_7_4_1/RelValZMM_13/GEN-SIM-RECO/MCRUN2_74_V9_gensim71X-v1/00000/3682F137-B9EC-E411-8D42-002618943876.root'
    ),
                            secondaryFileNames = cms.untracked.vstring()
                            )

process.MessageLogger = cms.Service("MessageLogger",
                                    debugModules = cms.untracked.vstring('*'),
                                    suppressDebug = cms.untracked.vstring('FwkJob', 'FwkReport'),
                                    suppressInfo = cms.untracked.vstring('FwkJob', 'FwkReport'),
                                    suppressWarning = cms.untracked.vstring('FwkJob', 'FwkReport'),
                                    cout = cms.untracked.PSet(threshold = cms.untracked.string('ERROR')),
                                    destinations = cms.untracked.vstring('cout')
                                    )

process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')
process.GlobalTag.globaltag = "MCRUN2_74_V9"

process.hltMenuVersionProvider =cms.EDAnalyzer("HLTMenuVersionProvider",
                                               hltProcessName = cms.untracked.string("HLT") 
                                               )
process.HLTMenuVersionProvider = cms.Path(process.hltMenuVersionProvider)

process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(-1))
