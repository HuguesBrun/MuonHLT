import FWCore.ParameterSet.Config as cms

process = cms.Process("HLTMENU")

process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring(
    '/store/data/Run2015B/SingleMuon/RECO/PromptReco-v1/000/251/252/00000/02F8A8CC-9527-E511-8223-02163E014437.root'
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
process.GlobalTag.globaltag = "GR_H_V58A"

process.hltMenuVersionProvider =cms.EDAnalyzer("HLTMenuVersionProvider",
                                               hltProcessName = cms.untracked.string("HLT") 
                                               )
process.HLTMenuVersionProvider = cms.Path(process.hltMenuVersionProvider)

process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(-1))
