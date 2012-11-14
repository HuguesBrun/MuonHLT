import FWCore.ParameterSet.Config as cms

process = cms.Process("RATE")

process.source = cms.Source("PoolSource",
                            # 2012B: 196452
                            ### Commissioning
#                             fileNames = cms.untracked.vstring(
#     '/store/data/Run2012B/Commissioning/RECO/PromptReco-v1/000/196/452/E6671F4E-15BA-E111-A6E7-BCAEC532971E.root',
#     '/store/data/Run2012B/Commissioning/RECO/PromptReco-v1/000/196/452/DE7B4BB7-D8B9-E111-ADDE-0025901D5D9A.root',
#     '/store/data/Run2012B/Commissioning/RECO/PromptReco-v1/000/196/452/D0682644-E7B9-E111-A716-00237DDC5C24.root',
#     '/store/data/Run2012B/Commissioning/RECO/PromptReco-v1/000/196/452/A81B1103-08BA-E111-94D2-001D09F253D4.root',
#     '/store/data/Run2012B/Commissioning/RECO/PromptReco-v1/000/196/452/9A59CB2B-2CBA-E111-9616-003048F11DE2.root',
#     '/store/data/Run2012B/Commissioning/RECO/PromptReco-v1/000/196/452/8C0586BF-3ABA-E111-8AA4-BCAEC518FF52.root',
#     '/store/data/Run2012B/Commissioning/RECO/PromptReco-v1/000/196/452/8272787C-23BA-E111-A989-BCAEC518FF80.root',
#     '/store/data/Run2012B/Commissioning/RECO/PromptReco-v1/000/196/452/7AE59537-35BA-E111-94D0-485B3962633D.root',
#     '/store/data/Run2012B/Commissioning/RECO/PromptReco-v1/000/196/452/780D53D3-29BA-E111-9787-BCAEC5364C42.root',
#     '/store/data/Run2012B/Commissioning/RECO/PromptReco-v1/000/196/452/6819BFEF-F5B9-E111-9410-003048D2BC38.root',
#     '/store/data/Run2012B/Commissioning/RECO/PromptReco-v1/000/196/452/52F63AEE-F5B9-E111-9FDC-003048F1C58C.root',
#     '/store/data/Run2012B/Commissioning/RECO/PromptReco-v1/000/196/452/48BEA9CE-01BA-E111-B31E-003048CF99BA.root',
#     '/store/data/Run2012B/Commissioning/RECO/PromptReco-v1/000/196/452/1E019436-D8B9-E111-9168-BCAEC532970D.root',
#     '/store/data/Run2012B/Commissioning/RECO/PromptReco-v1/000/196/452/140D8289-EFB9-E111-BAEB-001D09F2447F.root',
#     '/store/data/Run2012B/Commissioning/RECO/PromptReco-v1/000/196/452/125A74FD-D9B9-E111-8F6D-001D09F2910A.root',
#     '/store/data/Run2012B/Commissioning/RECO/PromptReco-v1/000/196/452/0C126F1D-0DBA-E111-AB77-5404A63886C6.root',
#     '/store/data/Run2012B/Commissioning/RECO/PromptReco-v1/000/196/452/02A412B1-FDB9-E111-BE6F-003048F11112.root',
#     ),
                            ### SingleMu
                            fileNames = cms.untracked.vstring(
    '/store/data/Run2012B/SingleMu/AOD/PromptReco-v1/000/196/452/FED0C0B6-52BA-E111-82B2-001D09F27003.root',
    '/store/data/Run2012B/SingleMu/AOD/PromptReco-v1/000/196/452/FC8E1F25-1ABA-E111-A2D4-003048D3C90E.root',
    '/store/data/Run2012B/SingleMu/AOD/PromptReco-v1/000/196/452/FAE79CCE-37BA-E111-BA16-BCAEC5329713.root',
    '/store/data/Run2012B/SingleMu/AOD/PromptReco-v1/000/196/452/FA4077A0-19BA-E111-8C44-BCAEC518FF52.root',
    '/store/data/Run2012B/SingleMu/AOD/PromptReco-v1/000/196/452/F66212CF-1DBA-E111-BF74-5404A640A63D.root',
    '/store/data/Run2012B/SingleMu/AOD/PromptReco-v1/000/196/452/F2F272C1-F3B9-E111-9967-003048CF94A8.root',
    '/store/data/Run2012B/SingleMu/AOD/PromptReco-v1/000/196/452/F2DF20BD-F3B9-E111-930F-003048F1C82A.root',
    '/store/data/Run2012B/SingleMu/AOD/PromptReco-v1/000/196/452/F24AD83F-21BA-E111-8D5F-BCAEC5329727.root',
    '/store/data/Run2012B/SingleMu/AOD/PromptReco-v1/000/196/452/F21D897F-EFB9-E111-9A12-001D09F2B2CF.root',
    '/store/data/Run2012B/SingleMu/AOD/PromptReco-v1/000/196/452/F0692024-ECB9-E111-B45A-BCAEC518FF74.root',
    '/store/data/Run2012B/SingleMu/AOD/PromptReco-v1/000/196/452/F00006C0-ECB9-E111-A8CA-001D09F28EA3.root',
    '/store/data/Run2012B/SingleMu/AOD/PromptReco-v1/000/196/452/EEFB6E26-47BA-E111-9C23-0030486730C6.root',
    '/store/data/Run2012B/SingleMu/AOD/PromptReco-v1/000/196/452/EE540C9B-3BBA-E111-B1C2-003048CF9B28.root',
    '/store/data/Run2012B/SingleMu/AOD/PromptReco-v1/000/196/452/ECEED28F-06BA-E111-8196-003048F024F6.root',
    '/store/data/Run2012B/SingleMu/AOD/PromptReco-v1/000/196/452/E699CBFC-23BA-E111-9E4D-003048D2BB58.root',
    '/store/data/Run2012B/SingleMu/AOD/PromptReco-v1/000/196/452/E2832866-0EBA-E111-809B-0025901D5C86.root',
    '/store/data/Run2012B/SingleMu/AOD/PromptReco-v1/000/196/452/E2054146-1BBA-E111-85AA-0025901D5DF4.root',
    '/store/data/Run2012B/SingleMu/AOD/PromptReco-v1/000/196/452/E0C4F71F-0ABA-E111-8914-BCAEC53296F4.root',
    '/store/data/Run2012B/SingleMu/AOD/PromptReco-v1/000/196/452/E0875CC6-1DBA-E111-80A6-5404A63886CB.root',
    '/store/data/Run2012B/SingleMu/AOD/PromptReco-v1/000/196/452/DE1C77F9-23BA-E111-AE19-BCAEC5329703.root',
    '/store/data/Run2012B/SingleMu/AOD/PromptReco-v1/000/196/452/DE05B36D-53BA-E111-BB8A-001D09F295FB.root',
    '/store/data/Run2012B/SingleMu/AOD/PromptReco-v1/000/196/452/DCB67EE0-EDB9-E111-A8C9-0025901D5DF4.root',
    '/store/data/Run2012B/SingleMu/AOD/PromptReco-v1/000/196/452/DA7BEF33-11BA-E111-A0DE-0030486780E6.root',
    '/store/data/Run2012B/SingleMu/AOD/PromptReco-v1/000/196/452/D87E2B9C-02BA-E111-BC26-001D09F2437B.root',
    '/store/data/Run2012B/SingleMu/AOD/PromptReco-v1/000/196/452/D8539C27-F5B9-E111-9CD8-001D09F2A465.root',
    '/store/data/Run2012B/SingleMu/AOD/PromptReco-v1/000/196/452/D6143595-2ABA-E111-AE04-5404A63886EF.root',
    '/store/data/Run2012B/SingleMu/AOD/PromptReco-v1/000/196/452/D2EB0422-ECB9-E111-A99F-BCAEC5329701.root',
    '/store/data/Run2012B/SingleMu/AOD/PromptReco-v1/000/196/452/CED53826-0FBA-E111-82A2-BCAEC518FF63.root',
    '/store/data/Run2012B/SingleMu/AOD/PromptReco-v1/000/196/452/CE9E83C1-ECB9-E111-9050-001D09F2906A.root',
    '/store/data/Run2012B/SingleMu/AOD/PromptReco-v1/000/196/452/CCD2C7E4-39BA-E111-A2F4-003048F1110E.root',
    '/store/data/Run2012B/SingleMu/AOD/PromptReco-v1/000/196/452/C810BA7F-22BA-E111-8A74-0030486730C6.root',
    '/store/data/Run2012B/SingleMu/AOD/PromptReco-v1/000/196/452/C2D1B943-DBB9-E111-9AED-001D09F28E80.root',
    '/store/data/Run2012B/SingleMu/AOD/PromptReco-v1/000/196/452/C0D2385E-F7B9-E111-B591-0025B3203898.root',
    '/store/data/Run2012B/SingleMu/AOD/PromptReco-v1/000/196/452/C00874A8-72BA-E111-91BC-003048D2BC5C.root',
    '/store/data/Run2012B/SingleMu/AOD/PromptReco-v1/000/196/452/BE1C0B2A-EEB9-E111-A450-003048D2BE08.root',
    '/store/data/Run2012B/SingleMu/AOD/PromptReco-v1/000/196/452/BCE74CE3-47BA-E111-B79A-001D09F2983F.root',
    '/store/data/Run2012B/SingleMu/AOD/PromptReco-v1/000/196/452/BCB52842-DBB9-E111-982F-003048678098.root',
    '/store/data/Run2012B/SingleMu/AOD/PromptReco-v1/000/196/452/BA643A28-4ABA-E111-A11C-001D09F25267.root',
    '/store/data/Run2012B/SingleMu/AOD/PromptReco-v1/000/196/452/B867796A-09BA-E111-8F59-BCAEC53296F7.root',
    '/store/data/Run2012B/SingleMu/AOD/PromptReco-v1/000/196/452/B4C2ABF7-D9B9-E111-8B15-5404A63886A0.root',
    '/store/data/Run2012B/SingleMu/AOD/PromptReco-v1/000/196/452/B435E0F5-51BA-E111-82A3-0025B32035A2.root',
    '/store/data/Run2012B/SingleMu/AOD/PromptReco-v1/000/196/452/B2EFB1B2-E3B9-E111-817C-001D09F24EE3.root',
    '/store/data/Run2012B/SingleMu/AOD/PromptReco-v1/000/196/452/B28A65E6-01BA-E111-B6BB-003048F118D2.root',
    '/store/data/Run2012B/SingleMu/AOD/PromptReco-v1/000/196/452/B099FDAF-EDB9-E111-BE56-E0CB4E4408E3.root',
    '/store/data/Run2012B/SingleMu/AOD/PromptReco-v1/000/196/452/B088F826-0FBA-E111-86E7-003048F1C424.root',
    '/store/data/Run2012B/SingleMu/AOD/PromptReco-v1/000/196/452/B0276035-F0B9-E111-A7B0-003048F118C2.root',
    '/store/data/Run2012B/SingleMu/AOD/PromptReco-v1/000/196/452/AE24CE87-1BBA-E111-AF73-003048D373F6.root',
    '/store/data/Run2012B/SingleMu/AOD/PromptReco-v1/000/196/452/AAE43092-0BBA-E111-87E1-0025901D624A.root',
    '/store/data/Run2012B/SingleMu/AOD/PromptReco-v1/000/196/452/AACCD64A-2EBA-E111-824D-003048D3C982.root',
    '/store/data/Run2012B/SingleMu/AOD/PromptReco-v1/000/196/452/AA9D0EC4-EDB9-E111-BFDE-001D09F29597.root',
    '/store/data/Run2012B/SingleMu/AOD/PromptReco-v1/000/196/452/A8D91F83-FCB9-E111-AB50-001D09F34488.root',
    '/store/data/Run2012B/SingleMu/AOD/PromptReco-v1/000/196/452/A63918C4-FBB9-E111-A2B1-003048F024F6.root',
    '/store/data/Run2012B/SingleMu/AOD/PromptReco-v1/000/196/452/A49C0C4B-EDB9-E111-A9E2-0025901D5DB2.root',
    '/store/data/Run2012B/SingleMu/AOD/PromptReco-v1/000/196/452/A23FDB42-DBB9-E111-AF9F-003048D2BBF0.root',
    '/store/data/Run2012B/SingleMu/AOD/PromptReco-v1/000/196/452/A04DCC82-2FBA-E111-9011-003048D2BC52.root',
    '/store/data/Run2012B/SingleMu/AOD/PromptReco-v1/000/196/452/A0074A5A-0CBA-E111-8003-BCAEC518FF76.root',
    '/store/data/Run2012B/SingleMu/AOD/PromptReco-v1/000/196/452/9A5CDA9D-02BA-E111-B508-001D09F251FE.root',
    '/store/data/Run2012B/SingleMu/AOD/PromptReco-v1/000/196/452/9839A86F-E2B9-E111-9187-003048F1C424.root',
    '/store/data/Run2012B/SingleMu/AOD/PromptReco-v1/000/196/452/96902FE4-F0B9-E111-8294-001D09F291D7.root',
    '/store/data/Run2012B/SingleMu/AOD/PromptReco-v1/000/196/452/94235EE1-EDB9-E111-A1FE-5404A63886B4.root',
    '/store/data/Run2012B/SingleMu/AOD/PromptReco-v1/000/196/452/92DEC379-27BA-E111-84B0-002481E0D524.root',
    '/store/data/Run2012B/SingleMu/AOD/PromptReco-v1/000/196/452/928E23AD-25BA-E111-9F01-003048F024C2.root',
    '/store/data/Run2012B/SingleMu/AOD/PromptReco-v1/000/196/452/9078BC90-02BA-E111-BF83-003048F11C58.root',
    '/store/data/Run2012B/SingleMu/AOD/PromptReco-v1/000/196/452/8EA954B1-EDB9-E111-9B22-5404A638869B.root',
    '/store/data/Run2012B/SingleMu/AOD/PromptReco-v1/000/196/452/8CF35335-F0B9-E111-A685-003048F117EA.root',
    '/store/data/Run2012B/SingleMu/AOD/PromptReco-v1/000/196/452/8CC5C930-E9B9-E111-BEF6-001D09F2462D.root',
    '/store/data/Run2012B/SingleMu/AOD/PromptReco-v1/000/196/452/8C6A3A94-0BBA-E111-9684-0025901D5C86.root',
    '/store/data/Run2012B/SingleMu/AOD/PromptReco-v1/000/196/452/8A335BED-01BA-E111-B8C9-003048D37524.root',
    '/store/data/Run2012B/SingleMu/AOD/PromptReco-v1/000/196/452/88BAA15A-1EBA-E111-86BD-BCAEC5329705.root',
    '/store/data/Run2012B/SingleMu/AOD/PromptReco-v1/000/196/452/80527BAA-F1B9-E111-BD4F-003048F118C2.root',
    '/store/data/Run2012B/SingleMu/AOD/PromptReco-v1/000/196/452/7EC460D7-0ABA-E111-B453-5404A63886D6.root',
    '/store/data/Run2012B/SingleMu/AOD/PromptReco-v1/000/196/452/7C816699-E7B9-E111-84CB-5404A63886AF.root',
    '/store/data/Run2012B/SingleMu/AOD/PromptReco-v1/000/196/452/7C67EC38-F0B9-E111-815A-001D09F290BF.root',
    '/store/data/Run2012B/SingleMu/AOD/PromptReco-v1/000/196/452/7C0F2531-17BA-E111-AF03-5404A63886EE.root',
    '/store/data/Run2012B/SingleMu/AOD/PromptReco-v1/000/196/452/7AE8AE90-EDB9-E111-BA3A-003048F118D4.root',
    '/store/data/Run2012B/SingleMu/AOD/PromptReco-v1/000/196/452/7AD2C49D-12BA-E111-A8F0-003048F118AC.root',
    '/store/data/Run2012B/SingleMu/AOD/PromptReco-v1/000/196/452/7880CF49-E7B9-E111-A606-002481E0D646.root',
    '/store/data/Run2012B/SingleMu/AOD/PromptReco-v1/000/196/452/74A6A270-07BA-E111-BB57-002481E0D958.root',
    '/store/data/Run2012B/SingleMu/AOD/PromptReco-v1/000/196/452/7445201C-0DBA-E111-B087-BCAEC518FF76.root',
    '/store/data/Run2012B/SingleMu/AOD/PromptReco-v1/000/196/452/72811157-29BA-E111-9C28-0025B320384C.root',
    '/store/data/Run2012B/SingleMu/AOD/PromptReco-v1/000/196/452/726C3E15-08BA-E111-9104-001D09F2906A.root',
    '/store/data/Run2012B/SingleMu/AOD/PromptReco-v1/000/196/452/70C7DF9A-E7B9-E111-BC3A-BCAEC518FF52.root',
    '/store/data/Run2012B/SingleMu/AOD/PromptReco-v1/000/196/452/70B7C762-F7B9-E111-B9B1-001D09F295FB.root',
    '/store/data/Run2012B/SingleMu/AOD/PromptReco-v1/000/196/452/70949A5C-0CBA-E111-AD7C-5404A63886EC.root',
    '/store/data/Run2012B/SingleMu/AOD/PromptReco-v1/000/196/452/70612073-07BA-E111-ACE3-5404A63886B1.root',
    '/store/data/Run2012B/SingleMu/AOD/PromptReco-v1/000/196/452/702BE9F0-3CBA-E111-A772-003048D37694.root',
    '/store/data/Run2012B/SingleMu/AOD/PromptReco-v1/000/196/452/701F771F-0ABA-E111-A432-5404A63886AF.root',
    '/store/data/Run2012B/SingleMu/AOD/PromptReco-v1/000/196/452/6CF80FC4-24BA-E111-B728-001D09F2932B.root',
    '/store/data/Run2012B/SingleMu/AOD/PromptReco-v1/000/196/452/6C852DC1-A4BA-E111-BD5E-001D09F27003.root',
    '/store/data/Run2012B/SingleMu/AOD/PromptReco-v1/000/196/452/68B6C1D6-0ABA-E111-9B11-BCAEC518FF74.root',
    '/store/data/Run2012B/SingleMu/AOD/PromptReco-v1/000/196/452/66CD3E43-02BA-E111-9318-002481E0D90C.root',
    '/store/data/Run2012B/SingleMu/AOD/PromptReco-v1/000/196/452/668E7FE2-EDB9-E111-AA39-0019B9F72D71.root',
    '/store/data/Run2012B/SingleMu/AOD/PromptReco-v1/000/196/452/6666A846-15BA-E111-8BEC-BCAEC5364CED.root',
    '/store/data/Run2012B/SingleMu/AOD/PromptReco-v1/000/196/452/62BA6F43-24BA-E111-8E40-003048F118D4.root',
    '/store/data/Run2012B/SingleMu/AOD/PromptReco-v1/000/196/452/62AD5E92-2ABA-E111-BF99-BCAEC518FF8F.root',
    '/store/data/Run2012B/SingleMu/AOD/PromptReco-v1/000/196/452/5E6904C6-1BBA-E111-8ADF-0030486730C6.root',
    '/store/data/Run2012B/SingleMu/AOD/PromptReco-v1/000/196/452/5E484250-F2B9-E111-B299-003048F118AA.root',
    '/store/data/Run2012B/SingleMu/AOD/PromptReco-v1/000/196/452/58665EB1-20BA-E111-8C64-E0CB4E553651.root',
    '/store/data/Run2012B/SingleMu/AOD/PromptReco-v1/000/196/452/56A71625-EDB9-E111-8319-001D09F29169.root',
    '/store/data/Run2012B/SingleMu/AOD/PromptReco-v1/000/196/452/548E8B6C-1EBA-E111-BF71-0025B32036E2.root',
    '/store/data/Run2012B/SingleMu/AOD/PromptReco-v1/000/196/452/5430B5EA-47BA-E111-AA45-003048673374.root',
    '/store/data/Run2012B/SingleMu/AOD/PromptReco-v1/000/196/452/52939DB5-2EBA-E111-BF85-5404A63886B7.root',
    '/store/data/Run2012B/SingleMu/AOD/PromptReco-v1/000/196/452/5000D361-46BA-E111-9ECB-0025901D623C.root',
    '/store/data/Run2012B/SingleMu/AOD/PromptReco-v1/000/196/452/4E3708C0-ECB9-E111-9283-001D09F23174.root',
    '/store/data/Run2012B/SingleMu/AOD/PromptReco-v1/000/196/452/4ACCA13D-21BA-E111-BB4B-BCAEC532971D.root',
    '/store/data/Run2012B/SingleMu/AOD/PromptReco-v1/000/196/452/4A41B93D-21BA-E111-BF57-0025901D5DEE.root',
    '/store/data/Run2012B/SingleMu/AOD/PromptReco-v1/000/196/452/48765494-EDB9-E111-822A-001D09F28D4A.root',
    '/store/data/Run2012B/SingleMu/AOD/PromptReco-v1/000/196/452/42E7999E-14BA-E111-9C33-003048F110BE.root',
    '/store/data/Run2012B/SingleMu/AOD/PromptReco-v1/000/196/452/3EC1ABA4-03BA-E111-8BD5-001D09F2527B.root',
    '/store/data/Run2012B/SingleMu/AOD/PromptReco-v1/000/196/452/3C8FE66B-F4B9-E111-94D7-002481E0DEC6.root',
    '/store/data/Run2012B/SingleMu/AOD/PromptReco-v1/000/196/452/38E81D09-F3B9-E111-9966-001D09F29114.root',
    '/store/data/Run2012B/SingleMu/AOD/PromptReco-v1/000/196/452/36C1CB81-22BA-E111-975C-485B3962633D.root',
    '/store/data/Run2012B/SingleMu/AOD/PromptReco-v1/000/196/452/3640684B-EDB9-E111-BDB7-5404A63886B2.root',
    '/store/data/Run2012B/SingleMu/AOD/PromptReco-v1/000/196/452/3403496A-09BA-E111-A282-485B39897227.root',
    '/store/data/Run2012B/SingleMu/AOD/PromptReco-v1/000/196/452/30C050D0-0FBA-E111-A891-003048F118C4.root',
    '/store/data/Run2012B/SingleMu/AOD/PromptReco-v1/000/196/452/30699915-1FBA-E111-9C19-001D09F2841C.root',
    '/store/data/Run2012B/SingleMu/AOD/PromptReco-v1/000/196/452/2E7AB97B-48BA-E111-86F5-0025901D625A.root',
    '/store/data/Run2012B/SingleMu/AOD/PromptReco-v1/000/196/452/2C676F8A-DAB9-E111-B262-BCAEC53296F3.root',
    '/store/data/Run2012B/SingleMu/AOD/PromptReco-v1/000/196/452/26B9F236-F0B9-E111-8B4D-001D09F2906A.root',
    '/store/data/Run2012B/SingleMu/AOD/PromptReco-v1/000/196/452/22380E6C-1ABA-E111-A720-0025901D5C86.root',
    '/store/data/Run2012B/SingleMu/AOD/PromptReco-v1/000/196/452/20C6E94A-2EBA-E111-85BE-003048D374CA.root',
    '/store/data/Run2012B/SingleMu/AOD/PromptReco-v1/000/196/452/2035EDAE-E9B9-E111-935E-003048D2BE06.root',
    '/store/data/Run2012B/SingleMu/AOD/PromptReco-v1/000/196/452/1EC780DF-DBB9-E111-A72E-001D09F290CE.root',
    '/store/data/Run2012B/SingleMu/AOD/PromptReco-v1/000/196/452/1E8E0EA4-26BA-E111-A7C9-5404A63886B0.root',
    '/store/data/Run2012B/SingleMu/AOD/PromptReco-v1/000/196/452/1C08CFCD-0FBA-E111-BC30-003048F117F6.root',
    '/store/data/Run2012B/SingleMu/AOD/PromptReco-v1/000/196/452/1AC39738-D8B9-E111-BA4B-485B39897227.root',
    '/store/data/Run2012B/SingleMu/AOD/PromptReco-v1/000/196/452/18D8DBFD-15BA-E111-AD2E-0025901D5D90.root',
    '/store/data/Run2012B/SingleMu/AOD/PromptReco-v1/000/196/452/1872B60F-08BA-E111-AA57-0019B9F581C9.root',
    '/store/data/Run2012B/SingleMu/AOD/PromptReco-v1/000/196/452/185EA8C8-EEB9-E111-85E7-003048F024F6.root',
    '/store/data/Run2012B/SingleMu/AOD/PromptReco-v1/000/196/452/1852D12C-EBB9-E111-A8DF-001D09F2A465.root',
    '/store/data/Run2012B/SingleMu/AOD/PromptReco-v1/000/196/452/141E64AD-F1B9-E111-81EB-003048D3756A.root',
    '/store/data/Run2012B/SingleMu/AOD/PromptReco-v1/000/196/452/1244A5FF-EEB9-E111-9724-001D09F2305C.root',
    '/store/data/Run2012B/SingleMu/AOD/PromptReco-v1/000/196/452/10E1B21A-EAB9-E111-842F-BCAEC532970F.root',
    '/store/data/Run2012B/SingleMu/AOD/PromptReco-v1/000/196/452/0E16827A-ECB9-E111-866D-BCAEC518FF7A.root',
    '/store/data/Run2012B/SingleMu/AOD/PromptReco-v1/000/196/452/0C9B0078-10BA-E111-8FE9-003048D374F2.root',
    '/store/data/Run2012B/SingleMu/AOD/PromptReco-v1/000/196/452/08F9ECE0-EDB9-E111-9619-0025901D631E.root',
    '/store/data/Run2012B/SingleMu/AOD/PromptReco-v1/000/196/452/0830DE5B-04BA-E111-A350-0030486780B4.root',
    '/store/data/Run2012B/SingleMu/AOD/PromptReco-v1/000/196/452/00479750-F2B9-E111-BAA5-002481E0D790.root',
    ),
                            # 2012C: 199319
                            ### Commissioning
#                             fileNames = cms.untracked.vstring(
#     '/store/data/Run2012C/Commissioning/RECO/PromptReco-v2/000/199/319/E66F789D-31D4-E111-9D70-E0CB4E55365C.root',
#     '/store/data/Run2012C/Commissioning/RECO/PromptReco-v2/000/199/319/D42C98DB-4BD4-E111-9B15-BCAEC5329717.root',
#     '/store/data/Run2012C/Commissioning/RECO/PromptReco-v2/000/199/319/C849CC69-4BD4-E111-AEFA-5404A63886D6.root',
#     '/store/data/Run2012C/Commissioning/RECO/PromptReco-v2/000/199/319/C042820D-38D4-E111-9CD3-5404A6388699.root',
#     '/store/data/Run2012C/Commissioning/RECO/PromptReco-v2/000/199/319/B090B9F6-6AD4-E111-8291-003048CF99BA.root',
#     '/store/data/Run2012C/Commissioning/RECO/PromptReco-v2/000/199/319/AEAB037A-3ED4-E111-9519-003048CF9B28.root',
#     '/store/data/Run2012C/Commissioning/RECO/PromptReco-v2/000/199/319/A6D09EEE-61D4-E111-A783-BCAEC518FF8E.root',
#     '/store/data/Run2012C/Commissioning/RECO/PromptReco-v2/000/199/319/92035DE3-49D4-E111-B8AE-001D09F24763.root',
#     '/store/data/Run2012C/Commissioning/RECO/PromptReco-v2/000/199/319/90E0FE00-5FD4-E111-8FF0-5404A63886BD.root',
#     '/store/data/Run2012C/Commissioning/RECO/PromptReco-v2/000/199/319/86763099-54D4-E111-B76E-001D09F24763.root',
#     '/store/data/Run2012C/Commissioning/RECO/PromptReco-v2/000/199/319/840734EF-39D4-E111-A450-0025B32036E2.root',
#     '/store/data/Run2012C/Commissioning/RECO/PromptReco-v2/000/199/319/7C6E6015-4CD4-E111-A820-0025B32035A2.root',
#     '/store/data/Run2012C/Commissioning/RECO/PromptReco-v2/000/199/319/6AAAA6ED-67D4-E111-BF5D-003048D2BF1C.root',
#     '/store/data/Run2012C/Commissioning/RECO/PromptReco-v2/000/199/319/689EAFB6-35D4-E111-B9DE-5404A63886B7.root',
#     '/store/data/Run2012C/Commissioning/RECO/PromptReco-v2/000/199/319/5CD43F0F-37D4-E111-A691-5404A63886B2.root',
#     '/store/data/Run2012C/Commissioning/RECO/PromptReco-v2/000/199/319/4AFC9053-36D4-E111-A14C-003048F024C2.root',
#     '/store/data/Run2012C/Commissioning/RECO/PromptReco-v2/000/199/319/3C9B70A2-4ED4-E111-A05D-001D09F28E80.root',
#     '/store/data/Run2012C/Commissioning/RECO/PromptReco-v2/000/199/319/3ABEFD30-5DD4-E111-9E09-001D09F2AF96.root',
#     '/store/data/Run2012C/Commissioning/RECO/PromptReco-v2/000/199/319/240AE3BF-5DD4-E111-8755-BCAEC5329713.root',
#     '/store/data/Run2012C/Commissioning/RECO/PromptReco-v2/000/199/319/22495FAA-37D4-E111-9D1A-003048F1BF68.root',
#     ),
                            ### SingleMu
#                             fileNames = cms.untracked.vstring(
#     '/store/data/Run2012C/SingleMu/AOD/PromptReco-v2/000/199/319/FEE6C9D8-47D4-E111-BB3F-003048D2BE06.root',
#     '/store/data/Run2012C/SingleMu/AOD/PromptReco-v2/000/199/319/FE5EFB2A-65D4-E111-A394-BCAEC518FF41.root',
#     '/store/data/Run2012C/SingleMu/AOD/PromptReco-v2/000/199/319/FCC33E9A-77D4-E111-A50B-003048D2C01A.root',
#     '/store/data/Run2012C/SingleMu/AOD/PromptReco-v2/000/199/319/FC4707FF-4DD4-E111-9A8D-0025901D5D80.root',
#     '/store/data/Run2012C/SingleMu/AOD/PromptReco-v2/000/199/319/F831DF4C-3DD4-E111-BBF1-BCAEC5329719.root',
#     '/store/data/Run2012C/SingleMu/AOD/PromptReco-v2/000/199/319/F089787D-87D4-E111-B4C2-001D09F24EE3.root',
#     '/store/data/Run2012C/SingleMu/AOD/PromptReco-v2/000/199/319/F010F118-4CD4-E111-9654-001D09F241F0.root',
#     '/store/data/Run2012C/SingleMu/AOD/PromptReco-v2/000/199/319/EADBE1C0-48D4-E111-9C07-5404A63886AE.root',
#     '/store/data/Run2012C/SingleMu/AOD/PromptReco-v2/000/199/319/EA6EDF15-63D4-E111-BD33-0025901D5DEE.root',
#     '/store/data/Run2012C/SingleMu/AOD/PromptReco-v2/000/199/319/EA229667-42D4-E111-A6D7-003048CF94A6.root',
#     '/store/data/Run2012C/SingleMu/AOD/PromptReco-v2/000/199/319/E89E330C-81D4-E111-9AA9-003048D3C982.root',
#     '/store/data/Run2012C/SingleMu/AOD/PromptReco-v2/000/199/319/E8165B65-6AD4-E111-AA95-003048D37580.root',
#     '/store/data/Run2012C/SingleMu/AOD/PromptReco-v2/000/199/319/E6B3DAC9-81D4-E111-8EF7-003048D3C982.root',
#     '/store/data/Run2012C/SingleMu/AOD/PromptReco-v2/000/199/319/E43D4164-3FD4-E111-A50D-001D09F2441B.root',
#     '/store/data/Run2012C/SingleMu/AOD/PromptReco-v2/000/199/319/E28D638F-53D4-E111-AB1E-BCAEC532971D.root',
#     '/store/data/Run2012C/SingleMu/AOD/PromptReco-v2/000/199/319/DE56DEF4-67D4-E111-B757-0025901D6268.root',
#     '/store/data/Run2012C/SingleMu/AOD/PromptReco-v2/000/199/319/DE522A60-55D4-E111-A74E-BCAEC5364C4C.root',
#     '/store/data/Run2012C/SingleMu/AOD/PromptReco-v2/000/199/319/DAEC92B9-48D4-E111-BCF8-485B39897227.root',
#     '/store/data/Run2012C/SingleMu/AOD/PromptReco-v2/000/199/319/DABB106F-55D4-E111-AF00-0030486780E6.root',
#     '/store/data/Run2012C/SingleMu/AOD/PromptReco-v2/000/199/319/D66C21E3-46D4-E111-A9F0-485B3962633D.root',
#     '/store/data/Run2012C/SingleMu/AOD/PromptReco-v2/000/199/319/D63BC1F9-4DD4-E111-8F86-0025901D62A6.root',
#     '/store/data/Run2012C/SingleMu/AOD/PromptReco-v2/000/199/319/D2EECBF5-60D4-E111-8902-003048F024FE.root',
#     '/store/data/Run2012C/SingleMu/AOD/PromptReco-v2/000/199/319/D29EAA65-3FD4-E111-884D-001D09F29146.root',
#     '/store/data/Run2012C/SingleMu/AOD/PromptReco-v2/000/199/319/D0F57F7C-6CD4-E111-A5AB-003048F1C82A.root',
#     '/store/data/Run2012C/SingleMu/AOD/PromptReco-v2/000/199/319/D0CF0184-40D4-E111-8076-5404A63886C0.root',
#     '/store/data/Run2012C/SingleMu/AOD/PromptReco-v2/000/199/319/D0B7D97F-3ED4-E111-B308-0025901D627C.root',
#     '/store/data/Run2012C/SingleMu/AOD/PromptReco-v2/000/199/319/D02836A6-54D4-E111-A25D-0025901D5DEE.root',
#     '/store/data/Run2012C/SingleMu/AOD/PromptReco-v2/000/199/319/CE1AFD00-52D4-E111-AAED-BCAEC5329727.root',
#     '/store/data/Run2012C/SingleMu/AOD/PromptReco-v2/000/199/319/C67A40FC-7ED4-E111-9AB6-003048673374.root',
#     '/store/data/Run2012C/SingleMu/AOD/PromptReco-v2/000/199/319/C4D47F55-66D4-E111-AF0A-0025901D5C86.root',
#     '/store/data/Run2012C/SingleMu/AOD/PromptReco-v2/000/199/319/C20D8413-63D4-E111-A663-BCAEC518FF52.root',
#     '/store/data/Run2012C/SingleMu/AOD/PromptReco-v2/000/199/319/BAF20FDB-73D4-E111-B4F3-BCAEC518FF41.root',
#     '/store/data/Run2012C/SingleMu/AOD/PromptReco-v2/000/199/319/BA3418A5-3CD4-E111-AAE8-001D09F242EF.root',
#     '/store/data/Run2012C/SingleMu/AOD/PromptReco-v2/000/199/319/B8E48780-3ED4-E111-A469-BCAEC5329727.root',
#     '/store/data/Run2012C/SingleMu/AOD/PromptReco-v2/000/199/319/B6DEB84D-4DD4-E111-8196-0025901D624A.root',
#     '/store/data/Run2012C/SingleMu/AOD/PromptReco-v2/000/199/319/B20FF500-68D4-E111-ACC1-001D09F2A465.root',
#     '/store/data/Run2012C/SingleMu/AOD/PromptReco-v2/000/199/319/B2080810-70D4-E111-8DDA-003048F1C832.root',
#     '/store/data/Run2012C/SingleMu/AOD/PromptReco-v2/000/199/319/B04DE6C5-6BD4-E111-8197-5404A63886CC.root',
#     '/store/data/Run2012C/SingleMu/AOD/PromptReco-v2/000/199/319/B01FA8A4-4ED4-E111-BD0A-5404A63886AF.root',
#     '/store/data/Run2012C/SingleMu/AOD/PromptReco-v2/000/199/319/AC7E1D81-65D4-E111-8E9B-003048F1C420.root',
#     '/store/data/Run2012C/SingleMu/AOD/PromptReco-v2/000/199/319/A807ABFF-6AD4-E111-9B01-0025901D627C.root',
#     '/store/data/Run2012C/SingleMu/AOD/PromptReco-v2/000/199/319/A6024CAF-53D4-E111-B7C1-003048D2BF1C.root',
#     '/store/data/Run2012C/SingleMu/AOD/PromptReco-v2/000/199/319/A41C23A8-70D4-E111-A7E6-001D09F2A465.root',
#     '/store/data/Run2012C/SingleMu/AOD/PromptReco-v2/000/199/319/A2B98C4E-4DD4-E111-92B7-0025901D6288.root',
#     '/store/data/Run2012C/SingleMu/AOD/PromptReco-v2/000/199/319/A201246A-43D4-E111-8404-0025901D5C88.root',
#     '/store/data/Run2012C/SingleMu/AOD/PromptReco-v2/000/199/319/A027368D-53D4-E111-BCFA-BCAEC53296F8.root',
#     '/store/data/Run2012C/SingleMu/AOD/PromptReco-v2/000/199/319/A00064E7-47D4-E111-87C7-0025901D5C86.root',
#     '/store/data/Run2012C/SingleMu/AOD/PromptReco-v2/000/199/319/9E9B8449-59D4-E111-A2A5-5404A63886AF.root',
#     '/store/data/Run2012C/SingleMu/AOD/PromptReco-v2/000/199/319/9ACD8810-38D4-E111-93C8-003048D2C174.root',
#     '/store/data/Run2012C/SingleMu/AOD/PromptReco-v2/000/199/319/988F4B65-42D4-E111-ACCD-00237DDC5CB0.root',
#     '/store/data/Run2012C/SingleMu/AOD/PromptReco-v2/000/199/319/96C65BBB-5BD4-E111-A459-003048F118D2.root',
#     '/store/data/Run2012C/SingleMu/AOD/PromptReco-v2/000/199/319/9653A08D-53D4-E111-88CC-5404A63886CF.root',
#     '/store/data/Run2012C/SingleMu/AOD/PromptReco-v2/000/199/319/94829A9D-85D4-E111-BF9B-001D09F24682.root',
#     '/store/data/Run2012C/SingleMu/AOD/PromptReco-v2/000/199/319/90B50F49-6DD4-E111-BD33-001D09F24353.root',
#     '/store/data/Run2012C/SingleMu/AOD/PromptReco-v2/000/199/319/9071E1F1-6DD4-E111-B9FB-001D09F2305C.root',
#     '/store/data/Run2012C/SingleMu/AOD/PromptReco-v2/000/199/319/8ECE90E1-46D4-E111-BBB4-BCAEC5364CFB.root',
#     '/store/data/Run2012C/SingleMu/AOD/PromptReco-v2/000/199/319/8E5BB31F-77D4-E111-9DD3-001D09F29321.root',
#     '/store/data/Run2012C/SingleMu/AOD/PromptReco-v2/000/199/319/882F80BC-5DD4-E111-9C5F-002481E0D958.root',
#     '/store/data/Run2012C/SingleMu/AOD/PromptReco-v2/000/199/319/86F8FB5C-66D4-E111-8287-001D09F295A1.root',
#     '/store/data/Run2012C/SingleMu/AOD/PromptReco-v2/000/199/319/8263E8B8-48D4-E111-823E-BCAEC518FF7A.root',
#     '/store/data/Run2012C/SingleMu/AOD/PromptReco-v2/000/199/319/7E1B4FB5-54D4-E111-BECA-001D09F2AF96.root',
#     '/store/data/Run2012C/SingleMu/AOD/PromptReco-v2/000/199/319/7C1441FC-7ED4-E111-89B6-0030486780AC.root',
#     '/store/data/Run2012C/SingleMu/AOD/PromptReco-v2/000/199/319/7AD14F65-6AD4-E111-8BF8-001D09F2AD4D.root',
#     '/store/data/Run2012C/SingleMu/AOD/PromptReco-v2/000/199/319/76469815-56D4-E111-A8FD-003048F1C836.root',
#     '/store/data/Run2012C/SingleMu/AOD/PromptReco-v2/000/199/319/6E5BC955-50D4-E111-96AE-002481E0D90C.root',
#     '/store/data/Run2012C/SingleMu/AOD/PromptReco-v2/000/199/319/6C68959C-9BD4-E111-B23B-0025901D62A6.root',
#     '/store/data/Run2012C/SingleMu/AOD/PromptReco-v2/000/199/319/68C9656A-5AD4-E111-87DE-0025901D6272.root',
#     '/store/data/Run2012C/SingleMu/AOD/PromptReco-v2/000/199/319/6818101B-4CD4-E111-8C7C-001D09F2841C.root',
#     '/store/data/Run2012C/SingleMu/AOD/PromptReco-v2/000/199/319/64DF2E58-4BD4-E111-BAA1-BCAEC5364CFB.root',
#     '/store/data/Run2012C/SingleMu/AOD/PromptReco-v2/000/199/319/6471C5D3-47D4-E111-A3D8-0030486780AC.root',
#     '/store/data/Run2012C/SingleMu/AOD/PromptReco-v2/000/199/319/629DDE4D-3FD4-E111-AC7D-0025901D624E.root',
#     '/store/data/Run2012C/SingleMu/AOD/PromptReco-v2/000/199/319/601D6054-66D4-E111-9311-BCAEC518FF65.root',
#     '/store/data/Run2012C/SingleMu/AOD/PromptReco-v2/000/199/319/5E311FEA-3BD4-E111-A997-003048D373AE.root',
#     '/store/data/Run2012C/SingleMu/AOD/PromptReco-v2/000/199/319/5661E8C2-49D4-E111-97F6-BCAEC532970F.root',
#     '/store/data/Run2012C/SingleMu/AOD/PromptReco-v2/000/199/319/54920985-6ED4-E111-814E-0025B32445E0.root',
#     '/store/data/Run2012C/SingleMu/AOD/PromptReco-v2/000/199/319/50C94A7C-6CD4-E111-AED4-003048F11942.root',
#     '/store/data/Run2012C/SingleMu/AOD/PromptReco-v2/000/199/319/50023454-6DD4-E111-B0B5-0025901D631E.root',
#     '/store/data/Run2012C/SingleMu/AOD/PromptReco-v2/000/199/319/4EEB522B-3BD4-E111-B34E-003048F1C82A.root',
#     '/store/data/Run2012C/SingleMu/AOD/PromptReco-v2/000/199/319/4E006D36-79D4-E111-B88D-0019B9F72F97.root',
#     '/store/data/Run2012C/SingleMu/AOD/PromptReco-v2/000/199/319/4698EA16-40D4-E111-B2BC-5404A640A642.root',
#     '/store/data/Run2012C/SingleMu/AOD/PromptReco-v2/000/199/319/42EA96C2-6CD4-E111-ADA5-BCAEC53296F3.root',
#     '/store/data/Run2012C/SingleMu/AOD/PromptReco-v2/000/199/319/3EEA9BBB-9AD4-E111-BF29-002481E0D958.root',
#     '/store/data/Run2012C/SingleMu/AOD/PromptReco-v2/000/199/319/3E9F63E6-57D4-E111-B6A5-5404A63886D2.root',
#     '/store/data/Run2012C/SingleMu/AOD/PromptReco-v2/000/199/319/3E3CA2A4-4AD4-E111-8B34-BCAEC518FF7A.root',
#     '/store/data/Run2012C/SingleMu/AOD/PromptReco-v2/000/199/319/3AB2F689-6CD4-E111-8643-003048D2C01E.root',
#     '/store/data/Run2012C/SingleMu/AOD/PromptReco-v2/000/199/319/3AA45637-86D4-E111-B2DE-0025901D626C.root',
#     '/store/data/Run2012C/SingleMu/AOD/PromptReco-v2/000/199/319/36B1A362-55D4-E111-B6FB-5404A63886C0.root',
#     '/store/data/Run2012C/SingleMu/AOD/PromptReco-v2/000/199/319/34CD5A0D-84D4-E111-ABE2-5404A638869C.root',
#     '/store/data/Run2012C/SingleMu/AOD/PromptReco-v2/000/199/319/34B159FC-61D4-E111-B7F1-485B3977172C.root',
#     '/store/data/Run2012C/SingleMu/AOD/PromptReco-v2/000/199/319/3450F9FC-5ED4-E111-93EE-001D09F2906A.root',
#     '/store/data/Run2012C/SingleMu/AOD/PromptReco-v2/000/199/319/32EFC064-6AD4-E111-88AF-001D09F23174.root',
#     '/store/data/Run2012C/SingleMu/AOD/PromptReco-v2/000/199/319/3082F420-49D4-E111-9114-BCAEC532970D.root',
#     '/store/data/Run2012C/SingleMu/AOD/PromptReco-v2/000/199/319/2EEB45E3-5FD4-E111-BD8B-BCAEC532971D.root',
#     '/store/data/Run2012C/SingleMu/AOD/PromptReco-v2/000/199/319/2AD74292-44D4-E111-8A85-BCAEC532971C.root',
#     '/store/data/Run2012C/SingleMu/AOD/PromptReco-v2/000/199/319/2AD58F75-39D4-E111-82A2-BCAEC518FF50.root',
#     '/store/data/Run2012C/SingleMu/AOD/PromptReco-v2/000/199/319/248A7B08-6BD4-E111-800F-003048CF9B28.root',
#     '/store/data/Run2012C/SingleMu/AOD/PromptReco-v2/000/199/319/24272EA8-4ED4-E111-8ED1-E0CB4E5536AE.root',
#     '/store/data/Run2012C/SingleMu/AOD/PromptReco-v2/000/199/319/2090873E-45D4-E111-9772-5404A63886AF.root',
#     '/store/data/Run2012C/SingleMu/AOD/PromptReco-v2/000/199/319/1A9C9400-52D4-E111-B6F9-BCAEC532971B.root',
#     '/store/data/Run2012C/SingleMu/AOD/PromptReco-v2/000/199/319/1A1F307C-58D4-E111-9C7A-001D09F23174.root',
#     '/store/data/Run2012C/SingleMu/AOD/PromptReco-v2/000/199/319/1852D0BA-48D4-E111-9A59-BCAEC5329716.root',
#     '/store/data/Run2012C/SingleMu/AOD/PromptReco-v2/000/199/319/1626A357-66D4-E111-8E37-BCAEC518FF6B.root',
#     '/store/data/Run2012C/SingleMu/AOD/PromptReco-v2/000/199/319/14E2DC7E-5AD4-E111-8180-5404A63886D4.root',
#     '/store/data/Run2012C/SingleMu/AOD/PromptReco-v2/000/199/319/14754A88-6ED4-E111-9F65-001D09F2B2CF.root',
#     '/store/data/Run2012C/SingleMu/AOD/PromptReco-v2/000/199/319/129B322C-64D4-E111-8B2B-003048F118C6.root',
#     '/store/data/Run2012C/SingleMu/AOD/PromptReco-v2/000/199/319/122605FE-61D4-E111-A100-BCAEC5364C93.root',
#     '/store/data/Run2012C/SingleMu/AOD/PromptReco-v2/000/199/319/08885084-65D4-E111-BFA0-003048CF9B28.root',
#     '/store/data/Run2012C/SingleMu/AOD/PromptReco-v2/000/199/319/023198BB-48D4-E111-95AC-5404A63886BD.root',
#     ),
                            secondaryFileNames = cms.untracked.vstring()
                            )

process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
#process.GlobalTag.globaltag = "GR_R_52_V7::All"
process.GlobalTag.globaltag = "GR_P_V32::All"

process.HLTCounter =cms.EDAnalyzer("HLTCounter",
                                   hltProcessName = cms.untracked.string("HLT"),         # from collection: edmTriggerResults_TriggerResults__HLT
                                   lumiProcessName = cms.untracked.string("RECO"),       # from collection: LumiScalerss_scalersRawToDigi__RECO
                                   lumiLabel = cms.untracked.string("scalersRawToDigi"), # from collection: LumiScalerss_scalersRawToDigi__RECO
                                   nLumisInAverage = cms.untracked.int32(1), # number of lumi-blocks to use for the compute the avarage rate
                                   NormIntLumi = cms.untracked.double(7000.0), # forgive about this parameter
                                   verbose = cms.untracked.bool(False), 
                                   printOutput = cms.untracked.bool(False), 
                                   useInstLumi = cms.untracked.bool(True), 
                                   printAtEndRun = cms.untracked.bool(True), 
                                   filterByOriginalHLTResults = cms.untracked.bool(False), # Set to 'True' if you want to use path in 'requiredOriginalPath' as reference 
                                   originalHLTName = cms.untracked.string("HLT"),          # from collection: edmTriggerResults_TriggerResults__HLT
                                   requiredOriginalPath = cms.untracked.string("HLT_L1SingleMu12_v"), # Reference path, only relevant if 'filterByOriginalHLTResults' is True
                                   FileName = cms.untracked.string("rates_2012B_isomu24_mu40.root"), # Output file name
                                   ListOfPaths = cms.untracked.vstring("HLT_IsoMu24_v", "HLT_Mu40_v"), # List of paths for which you want to compute rate
                                   )
process.HLTCountPath = cms.Path(process.HLTCounter)

process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(-1))
