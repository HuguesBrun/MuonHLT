import FWCore.ParameterSet.Config as cms

process = cms.Process("HLTFILTERPATH")

# General config options
import FWCore.ParameterSet.VarParsing as VarParsing
options = VarParsing.VarParsing()

options.register( 'globalTag',
                  'POSTLS162_V2::All', #default value
                  VarParsing.VarParsing.multiplicity.singleton,
                  VarParsing.VarParsing.varType.string,
                  "Global Tag")

options.register( 'hltPaths',
                  'HLT_L1SingleMu12', #default value
                  VarParsing.VarParsing.multiplicity.singleton,
                  VarParsing.VarParsing.varType.string,
                  "Paths to use for the skim")

options.parseArguments()

process.source = cms.Source( "PoolSource",
                             ## test TTbar file RAW-RECO skim from Fall13 production
                             fileNames = cms.untracked.vstring('/store/user/battilan/data/62X_RAW_RECO.root'),
                             secondaryFileNames = cms.untracked.vstring()
                             )

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

process.load('FWCore/MessageService/MessageLogger_cfi')

process.MessageLogger.cerr.FwkReport.reportEvery = 1000

process.options = cms.untracked.PSet(
    wantSummary = cms.untracked.bool( True )
)

process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
process.GlobalTag.globaltag = options.globalTag

process.triggerFilter = cms.EDFilter( "TriggerResultsFilter",
                                      triggerConditions = cms.vstring(options.hltPaths+'_v*'),
                                      hltResults = cms.InputTag( "TriggerResults", "", "HLT" ),
                                      l1tResults = cms.InputTag( "gtDigis" ),
                                      l1tIgnoreMask = cms.bool( False ),
                                      l1techIgnorePrescales = cms.bool( False ),
                                      daqPartitions = cms.uint32( 1 ),
                                      throw = cms.bool( True )
                                      )

process.triggerFilterPath = cms.Path(process.triggerFilter)

process.out = cms.OutputModule( "PoolOutputModule",
                                outputCommands = cms.untracked.vstring('keep *'),
                                fileName = cms.untracked.string('HLTFilterPath.root'),
                                SelectEvents = cms.untracked.PSet(SelectEvents = cms.vstring('triggerFilterPath') )
                               )

process.outPath = cms.EndPath(process.out)




