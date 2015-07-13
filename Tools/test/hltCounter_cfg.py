import FWCore.ParameterSet.Config as cms

process = cms.Process("RATE")

process.source = cms.Source("PoolSource",
                            ### SingleMu
                            fileNames = cms.untracked.vstring(
#    '/store/data/Run2012B/SingleMu/AOD/PromptReco-v1/000/196/452/FED0C0B6-52BA-E111-82B2-001D09F27003.root',
                                                              "/store/data/Run2015B/SingleMuon/RECO/PromptReco-v1/000/251/252/00000/02F8A8CC-9527-E511-8223-02163E014437.root",
                                                              "/store/data/Run2015B/SingleMuon/RECO/PromptReco-v1/000/251/252/00000/04014492-9327-E511-B61E-02163E0138A8.root",
                                                              "/store/data/Run2015B/SingleMuon/RECO/PromptReco-v1/000/251/252/00000/040DB4EF-9627-E511-BC70-02163E014437.root",
                                                              "/store/data/Run2015B/SingleMuon/RECO/PromptReco-v1/000/251/252/00000/0822AC7E-9227-E511-8FCE-02163E014629.root",
                                                              "/store/data/Run2015B/SingleMuon/RECO/PromptReco-v1/000/251/252/00000/0A67E1F8-9127-E511-9FFD-02163E012044.root",
                                                              "/store/data/Run2015B/SingleMuon/RECO/PromptReco-v1/000/251/252/00000/12AEE4A8-9927-E511-A8A6-02163E01413E.root",
                                                              "/store/data/Run2015B/SingleMuon/RECO/PromptReco-v1/000/251/252/00000/1A9D538D-8B27-E511-BEDB-02163E013422.root",
                                                              "/store/data/Run2015B/SingleMuon/RECO/PromptReco-v1/000/251/252/00000/1E07D09F-9327-E511-80F0-02163E011CE4.root",
                                                              "/store/data/Run2015B/SingleMuon/RECO/PromptReco-v1/000/251/252/00000/1EF0FE4E-9027-E511-8F1C-02163E014761.root",
                                                              "/store/data/Run2015B/SingleMuon/RECO/PromptReco-v1/000/251/252/00000/346EC53E-9627-E511-B1FE-02163E012073.root",
                                                              "/store/data/Run2015B/SingleMuon/RECO/PromptReco-v1/000/251/252/00000/3824B485-9227-E511-9CD0-02163E0135C9.root",
                                                              "/store/data/Run2015B/SingleMuon/RECO/PromptReco-v1/000/251/252/00000/3ADE4B61-9A27-E511-A961-02163E0143AA.root",
                                                              "/store/data/Run2015B/SingleMuon/RECO/PromptReco-v1/000/251/252/00000/4272F1CE-9527-E511-8D61-02163E013414.root",
                                                              "/store/data/Run2015B/SingleMuon/RECO/PromptReco-v1/000/251/252/00000/4C66C65C-9427-E511-8EAE-02163E011816.root",
                                                              "/store/data/Run2015B/SingleMuon/RECO/PromptReco-v1/000/251/252/00000/522317D2-9727-E511-A7E4-02163E014629.root",
                                                              "/store/data/Run2015B/SingleMuon/RECO/PromptReco-v1/000/251/252/00000/560B33F5-9427-E511-8A38-02163E0134A9.root",
                                                              "/store/data/Run2015B/SingleMuon/RECO/PromptReco-v1/000/251/252/00000/5C6B277C-A427-E511-B359-02163E012A7F.root",
                                                              "/store/data/Run2015B/SingleMuon/RECO/PromptReco-v1/000/251/252/00000/621550A7-9627-E511-897C-02163E01364E.root",
                                                              "/store/data/Run2015B/SingleMuon/RECO/PromptReco-v1/000/251/252/00000/70545C7F-A127-E511-B4A8-02163E014437.root",
                                                              "/store/data/Run2015B/SingleMuon/RECO/PromptReco-v1/000/251/252/00000/76E533D4-9727-E511-8D79-02163E011C7F.root",
                                                              "/store/data/Run2015B/SingleMuon/RECO/PromptReco-v1/000/251/252/00000/78209AA3-9327-E511-908F-02163E013414.root",
                                                              "/store/data/Run2015B/SingleMuon/RECO/PromptReco-v1/000/251/252/00000/7ACF7B47-9927-E511-863E-02163E0135F3.root",
                                                              "/store/data/Run2015B/SingleMuon/RECO/PromptReco-v1/000/251/252/00000/7AEFB075-9327-E511-A90C-02163E0136A2.root",
                                                              "/store/data/Run2015B/SingleMuon/RECO/PromptReco-v1/000/251/252/00000/88094278-9127-E511-9A69-02163E011CE4.root",
                                                              "/store/data/Run2015B/SingleMuon/RECO/PromptReco-v1/000/251/252/00000/942C1936-9627-E511-9330-02163E0133A4.root",
                                                              "/store/data/Run2015B/SingleMuon/RECO/PromptReco-v1/000/251/252/00000/9AEE9D88-9227-E511-999D-02163E0118BC.root",
                                                              "/store/data/Run2015B/SingleMuon/RECO/PromptReco-v1/000/251/252/00000/A43B5A82-9427-E511-B519-02163E013901.root",
                                                              "/store/data/Run2015B/SingleMuon/RECO/PromptReco-v1/000/251/252/00000/A47F3C18-9727-E511-A987-02163E0121BD.root",
                                                              "/store/data/Run2015B/SingleMuon/RECO/PromptReco-v1/000/251/252/00000/AA82A146-9627-E511-8F47-02163E012418.root",
                                                              "/store/data/Run2015B/SingleMuon/RECO/PromptReco-v1/000/251/252/00000/ACBCAF6D-8E27-E511-BC3A-02163E0133B6.root",
                                                              "/store/data/Run2015B/SingleMuon/RECO/PromptReco-v1/000/251/252/00000/ACF3745B-9527-E511-A3EB-02163E0143F8.root",
                                                              "/store/data/Run2015B/SingleMuon/RECO/PromptReco-v1/000/251/252/00000/AE39A17E-9427-E511-BED7-02163E012627.root",
                                                              "/store/data/Run2015B/SingleMuon/RECO/PromptReco-v1/000/251/252/00000/B4C5DB81-A127-E511-8E98-02163E0135F3.root",
                                                              "/store/data/Run2015B/SingleMuon/RECO/PromptReco-v1/000/251/252/00000/C069CCA3-9327-E511-8210-02163E012627.root",
                                                              "/store/data/Run2015B/SingleMuon/RECO/PromptReco-v1/000/251/252/00000/C0ED6A77-9327-E511-AAC4-02163E01186A.root",
                                                              "/store/data/Run2015B/SingleMuon/RECO/PromptReco-v1/000/251/252/00000/C2CCBD4C-9427-E511-9E1F-02163E011CD6.root",
                                                              "/store/data/Run2015B/SingleMuon/RECO/PromptReco-v1/000/251/252/00000/E0693E75-9427-E511-8210-02163E01186A.root",
                                                              "/store/data/Run2015B/SingleMuon/RECO/PromptReco-v1/000/251/252/00000/E289A2FD-9427-E511-B06B-02163E0118BC.root",
                                                              "/store/data/Run2015B/SingleMuon/RECO/PromptReco-v1/000/251/252/00000/ECAA1CFE-9427-E511-9CE3-02163E01413E.root",
                                                              "/store/data/Run2015B/SingleMuon/RECO/PromptReco-v1/000/251/252/00000/F2D20E33-9527-E511-B0BD-02163E011CE4.root",
                                                              "/store/data/Run2015B/SingleMuon/RECO/PromptReco-v1/000/251/252/00000/F457C9A2-9327-E511-82B7-02163E013576.root",
                                                              "/store/data/Run2015B/SingleMuon/RECO/PromptReco-v1/000/251/252/00000/F8A6335C-9527-E511-A862-02163E011C7F.root",
                                                              "/store/data/Run2015B/SingleMuon/RECO/PromptReco-v1/000/251/252/00000/FCDC2D40-9627-E511-9E6E-02163E013830.root",
                                                              "/store/data/Run2015B/SingleMuon/RECO/PromptReco-v1/000/251/252/00000/FEA69A26-9A27-E511-99CA-02163E01387D.root"    ),
                            secondaryFileNames = cms.untracked.vstring()
                            )

process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
from Configuration.AlCa.GlobalTag_condDBv2 import GlobalTag as customiseGlobalTag
process.GlobalTag = customiseGlobalTag(process.GlobalTag, globaltag = 'SPR1574_STV1')
process.GlobalTag.connect   = 'frontier://FrontierProd/CMS_CONDITIONS'
process.GlobalTag.pfnPrefix = cms.untracked.string('frontier://FrontierProd/')#process.GlobalTag.globaltag = "GR_H_V58A"

process.HLTCounter =cms.EDAnalyzer("HLTCounter",
                                   hltProcessName = cms.untracked.string("HLT"),         # from collection: edmTriggerResults_TriggerResults__HLT
                                   lumiProcessName = cms.untracked.string("RECO"),       # from collection: LumiScalerss_scalersRawToDigi__RECO
                                   lumiLabel = cms.untracked.string("scalersRawToDigi"), # from collection: LumiScalerss_scalersRawToDigi__RECO
                                   nLumisInAverage = cms.untracked.int32(1), # number of lumi-blocks to use for the compute the avarage rate
                                   NormIntLumi = cms.untracked.double(7000.0), # forgive about this parameter
                                   verbose = cms.untracked.bool(True), 
                                   printOutput = cms.untracked.bool(False), 
                                   useInstLumi = cms.untracked.bool(True), 
                                   printAtEndRun = cms.untracked.bool(True), 
                                   filterByOriginalHLTResults = cms.untracked.bool(False), # Set to 'True' if you want to use path in 'requiredOriginalPath' as reference 
                                   originalHLTName = cms.untracked.string("HLT"),          # from collection: edmTriggerResults_TriggerResults__HLT
                                   requiredOriginalPath = cms.untracked.string("HLT_L1SingleMu16_v"), # Reference path, only relevant if 'filterByOriginalHLTResults' is True
                                   FileName = cms.untracked.string("rates_2012B_IsoMu20.root"), # Output file name
                                   ListOfPaths = cms.untracked.vstring("HLT_IsoMu20_v"),#, "HLT_Mu20_v","HLT_L2Mu10_v","HLT_L1SingleMu16_v"), # List of paths for which you want to compute rate
                                   )
process.HLTCountPath = cms.Path(process.HLTCounter)

process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(1000))
