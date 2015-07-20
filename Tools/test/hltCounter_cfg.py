import FWCore.ParameterSet.Config as cms

process = cms.Process("RATE")

process.source = cms.Source("PoolSource",
                            ### SingleMu
                            fileNames = cms.untracked.vstring(
#    '/store/data/Run2012B/SingleMu/AOD/PromptReco-v1/000/196/452/FED0C0B6-52BA-E111-82B2-001D09F27003.root',
"/store/data/Run2015B/SingleMuon/RECO/PromptReco-v1/000/251/244/00000/064527E9-6827-E511-985C-02163E013746.root",
"/store/data/Run2015B/SingleMuon/RECO/PromptReco-v1/000/251/244/00000/08FABF77-6C27-E511-8B91-02163E01192D.root",
"/store/data/Run2015B/SingleMuon/RECO/PromptReco-v1/000/251/244/00000/0A144705-4B27-E511-8250-02163E01287D.root",
"/store/data/Run2015B/SingleMuon/RECO/PromptReco-v1/000/251/244/00000/12065B50-6F27-E511-88DB-02163E0144DA.root",
"/store/data/Run2015B/SingleMuon/RECO/PromptReco-v1/000/251/244/00000/24C1C811-5027-E511-9A0A-02163E014543.root",
"/store/data/Run2015B/SingleMuon/RECO/PromptReco-v1/000/251/244/00000/3045BAAE-5427-E511-AC6B-02163E0139A2.root",
"/store/data/Run2015B/SingleMuon/RECO/PromptReco-v1/000/251/244/00000/34C99B0E-4F27-E511-80AC-02163E011DCE.root",
"/store/data/Run2015B/SingleMuon/RECO/PromptReco-v1/000/251/244/00000/36B56210-6B27-E511-9C9F-02163E013674.root",
"/store/data/Run2015B/SingleMuon/RECO/PromptReco-v1/000/251/244/00000/36B9D499-5227-E511-B913-02163E011CD6.root",
"/store/data/Run2015B/SingleMuon/RECO/PromptReco-v1/000/251/244/00000/4043B82E-4627-E511-B2FD-02163E01415E.root",
"/store/data/Run2015B/SingleMuon/RECO/PromptReco-v1/000/251/244/00000/42529294-4F27-E511-BE20-02163E0127EF.root",
"/store/data/Run2015B/SingleMuon/RECO/PromptReco-v1/000/251/244/00000/4683C8F9-4727-E511-BA74-02163E0133F0.root",
"/store/data/Run2015B/SingleMuon/RECO/PromptReco-v1/000/251/244/00000/4E6EC95D-4A27-E511-95DD-02163E01364E.root",
"/store/data/Run2015B/SingleMuon/RECO/PromptReco-v1/000/251/244/00000/5003C6DF-5227-E511-B8AF-02163E01208E.root",
"/store/data/Run2015B/SingleMuon/RECO/PromptReco-v1/000/251/244/00000/50984099-5227-E511-8C57-02163E011BB9.root",
"/store/data/Run2015B/SingleMuon/RECO/PromptReco-v1/000/251/244/00000/54AAACAB-5427-E511-AD5D-02163E014144.root",
"/store/data/Run2015B/SingleMuon/RECO/PromptReco-v1/000/251/244/00000/56DF55AA-5227-E511-8BA1-02163E013598.root",
"/store/data/Run2015B/SingleMuon/RECO/PromptReco-v1/000/251/244/00000/5E171A72-7C27-E511-99EB-02163E012366.root",
"/store/data/Run2015B/SingleMuon/RECO/PromptReco-v1/000/251/244/00000/60EA58F9-4F27-E511-A5F4-02163E011CDB.root",
"/store/data/Run2015B/SingleMuon/RECO/PromptReco-v1/000/251/244/00000/7442597F-5827-E511-A2EB-02163E014616.root",
"/store/data/Run2015B/SingleMuon/RECO/PromptReco-v1/000/251/244/00000/7EAB9448-4F27-E511-917F-02163E0144CC.root",
"/store/data/Run2015B/SingleMuon/RECO/PromptReco-v1/000/251/244/00000/88AFB534-6627-E511-BA30-02163E012283.root",
"/store/data/Run2015B/SingleMuon/RECO/PromptReco-v1/000/251/244/00000/8C1F8764-6927-E511-AFD3-02163E0135AC.root",
"/store/data/Run2015B/SingleMuon/RECO/PromptReco-v1/000/251/244/00000/8CAA79A3-5227-E511-86E5-02163E011A29.root",
"/store/data/Run2015B/SingleMuon/RECO/PromptReco-v1/000/251/244/00000/9686FD04-5027-E511-8CFB-02163E013597.root",
"/store/data/Run2015B/SingleMuon/RECO/PromptReco-v1/000/251/244/00000/98064729-6527-E511-B8F6-02163E0145B2.root",
"/store/data/Run2015B/SingleMuon/RECO/PromptReco-v1/000/251/244/00000/98D44687-6627-E511-8DE3-02163E012158.root",
"/store/data/Run2015B/SingleMuon/RECO/PromptReco-v1/000/251/244/00000/9EC192A7-5227-E511-9CB7-02163E01445F.root",
"/store/data/Run2015B/SingleMuon/RECO/PromptReco-v1/000/251/244/00000/A432CEAC-4A27-E511-9611-02163E011816.root",
"/store/data/Run2015B/SingleMuon/RECO/PromptReco-v1/000/251/244/00000/A6AB3E40-4E27-E511-8037-02163E014558.root",
"/store/data/Run2015B/SingleMuon/RECO/PromptReco-v1/000/251/244/00000/A6DEFA49-5A27-E511-BB32-02163E013932.root",
"/store/data/Run2015B/SingleMuon/RECO/PromptReco-v1/000/251/244/00000/B23BA93A-5227-E511-92CF-02163E0144F6.root",
"/store/data/Run2015B/SingleMuon/RECO/PromptReco-v1/000/251/244/00000/B42D57C9-5D27-E511-93B3-02163E01420D.root",
"/store/data/Run2015B/SingleMuon/RECO/PromptReco-v1/000/251/244/00000/BA4C9B3C-7C27-E511-8EC8-02163E01420D.root",
"/store/data/Run2015B/SingleMuon/RECO/PromptReco-v1/000/251/244/00000/BA638E2B-6F27-E511-94BC-02163E0146D1.root",
"/store/data/Run2015B/SingleMuon/RECO/PromptReco-v1/000/251/244/00000/CA225D96-5227-E511-8018-02163E013455.root",
"/store/data/Run2015B/SingleMuon/RECO/PromptReco-v1/000/251/244/00000/E6BD112E-6827-E511-9FBA-02163E0135B4.root",
"/store/data/Run2015B/SingleMuon/RECO/PromptReco-v1/000/251/244/00000/E8D9002F-4127-E511-ADF7-02163E01413E.root",
"/store/data/Run2015B/SingleMuon/RECO/PromptReco-v1/000/251/244/00000/EA4DA198-5227-E511-9E57-02163E012073.root",
"/store/data/Run2015B/SingleMuon/RECO/PromptReco-v1/000/251/244/00000/EC99B8A1-5C27-E511-8143-02163E011BB9.root",
"/store/data/Run2015B/SingleMuon/RECO/PromptReco-v1/000/251/244/00000/F8F1DF12-6A27-E511-813A-02163E012283.root",
"/store/data/Run2015B/SingleMuon/RECO/PromptReco-v1/000/251/244/00000/FE87EAF8-4B27-E511-9CF8-02163E01259F.root"
),
                            secondaryFileNames = cms.untracked.vstring()
                            )

process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
from Configuration.AlCa.GlobalTag_condDBv2 import GlobalTag as customiseGlobalTag
process.GlobalTag = customiseGlobalTag(process.GlobalTag, globaltag = '74X_dataRun2_Prompt_v0')
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
                                   ListOfPaths = cms.untracked.vstring("HLT_IsoMu20_v","HLT_L2Mu10_v"),#, "HLT_Mu20_v","HLT_L2Mu10_v","HLT_L1SingleMu16_v"), # List of paths for which you want to compute rate
                                   )
process.HLTCountPath = cms.Path(process.HLTCounter)

process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(1000))
