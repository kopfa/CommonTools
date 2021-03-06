
import FWCore.ParameterSet.Config as cms

readFiles = cms.untracked.vstring()
source = cms.Source("PoolSource",
		     noEventSort = cms.untracked.bool(True),
		     duplicateCheckMode = cms.untracked.string("noDuplicateCheck"),
		     fileNames = readFiles
                    )
readFiles.extend([
	'rfio:///castor/cern.ch/user/t/tjkim/MC/Fall11/SingleElectron/DYJetsToLL_TuneZ2_M-50/patTuple_skim_100_0_clP.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MC/Fall11/SingleElectron/DYJetsToLL_TuneZ2_M-50/patTuple_skim_101_0_tEK.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MC/Fall11/SingleElectron/DYJetsToLL_TuneZ2_M-50/patTuple_skim_102_0_X0r.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MC/Fall11/SingleElectron/DYJetsToLL_TuneZ2_M-50/patTuple_skim_103_0_hhJ.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MC/Fall11/SingleElectron/DYJetsToLL_TuneZ2_M-50/patTuple_skim_104_0_wlN.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MC/Fall11/SingleElectron/DYJetsToLL_TuneZ2_M-50/patTuple_skim_105_0_gpZ.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MC/Fall11/SingleElectron/DYJetsToLL_TuneZ2_M-50/patTuple_skim_106_0_VmM.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MC/Fall11/SingleElectron/DYJetsToLL_TuneZ2_M-50/patTuple_skim_107_0_yeE.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MC/Fall11/SingleElectron/DYJetsToLL_TuneZ2_M-50/patTuple_skim_108_0_KJK.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MC/Fall11/SingleElectron/DYJetsToLL_TuneZ2_M-50/patTuple_skim_109_0_wDk.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MC/Fall11/SingleElectron/DYJetsToLL_TuneZ2_M-50/patTuple_skim_10_0_z7H.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MC/Fall11/SingleElectron/DYJetsToLL_TuneZ2_M-50/patTuple_skim_110_0_KTY.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MC/Fall11/SingleElectron/DYJetsToLL_TuneZ2_M-50/patTuple_skim_111_0_B2k.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MC/Fall11/SingleElectron/DYJetsToLL_TuneZ2_M-50/patTuple_skim_112_0_RXE.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MC/Fall11/SingleElectron/DYJetsToLL_TuneZ2_M-50/patTuple_skim_113_0_8nZ.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MC/Fall11/SingleElectron/DYJetsToLL_TuneZ2_M-50/patTuple_skim_114_0_aqr.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MC/Fall11/SingleElectron/DYJetsToLL_TuneZ2_M-50/patTuple_skim_115_0_I0k.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MC/Fall11/SingleElectron/DYJetsToLL_TuneZ2_M-50/patTuple_skim_116_0_y6c.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MC/Fall11/SingleElectron/DYJetsToLL_TuneZ2_M-50/patTuple_skim_117_0_gmf.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MC/Fall11/SingleElectron/DYJetsToLL_TuneZ2_M-50/patTuple_skim_118_0_oQk.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MC/Fall11/SingleElectron/DYJetsToLL_TuneZ2_M-50/patTuple_skim_119_0_uSy.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MC/Fall11/SingleElectron/DYJetsToLL_TuneZ2_M-50/patTuple_skim_11_0_V7B.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MC/Fall11/SingleElectron/DYJetsToLL_TuneZ2_M-50/patTuple_skim_120_0_Syn.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MC/Fall11/SingleElectron/DYJetsToLL_TuneZ2_M-50/patTuple_skim_121_0_Tot.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MC/Fall11/SingleElectron/DYJetsToLL_TuneZ2_M-50/patTuple_skim_122_0_MFa.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MC/Fall11/SingleElectron/DYJetsToLL_TuneZ2_M-50/patTuple_skim_123_0_2Rb.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MC/Fall11/SingleElectron/DYJetsToLL_TuneZ2_M-50/patTuple_skim_124_0_WBV.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MC/Fall11/SingleElectron/DYJetsToLL_TuneZ2_M-50/patTuple_skim_125_0_jwL.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MC/Fall11/SingleElectron/DYJetsToLL_TuneZ2_M-50/patTuple_skim_126_0_ico.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MC/Fall11/SingleElectron/DYJetsToLL_TuneZ2_M-50/patTuple_skim_127_0_9sa.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MC/Fall11/SingleElectron/DYJetsToLL_TuneZ2_M-50/patTuple_skim_12_0_qKP.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MC/Fall11/SingleElectron/DYJetsToLL_TuneZ2_M-50/patTuple_skim_133_0_b7z.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MC/Fall11/SingleElectron/DYJetsToLL_TuneZ2_M-50/patTuple_skim_134_0_nCw.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MC/Fall11/SingleElectron/DYJetsToLL_TuneZ2_M-50/patTuple_skim_135_0_AGx.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MC/Fall11/SingleElectron/DYJetsToLL_TuneZ2_M-50/patTuple_skim_136_0_YU7.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MC/Fall11/SingleElectron/DYJetsToLL_TuneZ2_M-50/patTuple_skim_137_0_ObY.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MC/Fall11/SingleElectron/DYJetsToLL_TuneZ2_M-50/patTuple_skim_138_0_QZh.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MC/Fall11/SingleElectron/DYJetsToLL_TuneZ2_M-50/patTuple_skim_139_0_qpD.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MC/Fall11/SingleElectron/DYJetsToLL_TuneZ2_M-50/patTuple_skim_13_0_7iE.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MC/Fall11/SingleElectron/DYJetsToLL_TuneZ2_M-50/patTuple_skim_140_0_bFo.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MC/Fall11/SingleElectron/DYJetsToLL_TuneZ2_M-50/patTuple_skim_141_0_b6u.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MC/Fall11/SingleElectron/DYJetsToLL_TuneZ2_M-50/patTuple_skim_142_0_0zL.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MC/Fall11/SingleElectron/DYJetsToLL_TuneZ2_M-50/patTuple_skim_143_0_MS7.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MC/Fall11/SingleElectron/DYJetsToLL_TuneZ2_M-50/patTuple_skim_145_0_XbU.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MC/Fall11/SingleElectron/DYJetsToLL_TuneZ2_M-50/patTuple_skim_146_0_SKZ.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MC/Fall11/SingleElectron/DYJetsToLL_TuneZ2_M-50/patTuple_skim_147_0_7Z3.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MC/Fall11/SingleElectron/DYJetsToLL_TuneZ2_M-50/patTuple_skim_148_0_G6D.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MC/Fall11/SingleElectron/DYJetsToLL_TuneZ2_M-50/patTuple_skim_149_0_9zf.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MC/Fall11/SingleElectron/DYJetsToLL_TuneZ2_M-50/patTuple_skim_14_0_rxk.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MC/Fall11/SingleElectron/DYJetsToLL_TuneZ2_M-50/patTuple_skim_150_0_YDh.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MC/Fall11/SingleElectron/DYJetsToLL_TuneZ2_M-50/patTuple_skim_151_0_GHF.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MC/Fall11/SingleElectron/DYJetsToLL_TuneZ2_M-50/patTuple_skim_152_0_ReK.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MC/Fall11/SingleElectron/DYJetsToLL_TuneZ2_M-50/patTuple_skim_153_0_wNC.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MC/Fall11/SingleElectron/DYJetsToLL_TuneZ2_M-50/patTuple_skim_154_0_cS8.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MC/Fall11/SingleElectron/DYJetsToLL_TuneZ2_M-50/patTuple_skim_155_0_NW3.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MC/Fall11/SingleElectron/DYJetsToLL_TuneZ2_M-50/patTuple_skim_156_0_uG5.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MC/Fall11/SingleElectron/DYJetsToLL_TuneZ2_M-50/patTuple_skim_157_0_TC5.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MC/Fall11/SingleElectron/DYJetsToLL_TuneZ2_M-50/patTuple_skim_158_0_h2O.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MC/Fall11/SingleElectron/DYJetsToLL_TuneZ2_M-50/patTuple_skim_159_0_Atz.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MC/Fall11/SingleElectron/DYJetsToLL_TuneZ2_M-50/patTuple_skim_15_1_rlD.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MC/Fall11/SingleElectron/DYJetsToLL_TuneZ2_M-50/patTuple_skim_160_0_r6s.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MC/Fall11/SingleElectron/DYJetsToLL_TuneZ2_M-50/patTuple_skim_161_0_ks4.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MC/Fall11/SingleElectron/DYJetsToLL_TuneZ2_M-50/patTuple_skim_162_0_OoL.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MC/Fall11/SingleElectron/DYJetsToLL_TuneZ2_M-50/patTuple_skim_163_0_EGE.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MC/Fall11/SingleElectron/DYJetsToLL_TuneZ2_M-50/patTuple_skim_164_0_aQs.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MC/Fall11/SingleElectron/DYJetsToLL_TuneZ2_M-50/patTuple_skim_165_0_jyo.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MC/Fall11/SingleElectron/DYJetsToLL_TuneZ2_M-50/patTuple_skim_166_0_3eD.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MC/Fall11/SingleElectron/DYJetsToLL_TuneZ2_M-50/patTuple_skim_167_0_YwI.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MC/Fall11/SingleElectron/DYJetsToLL_TuneZ2_M-50/patTuple_skim_168_0_k4f.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MC/Fall11/SingleElectron/DYJetsToLL_TuneZ2_M-50/patTuple_skim_169_0_5fF.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MC/Fall11/SingleElectron/DYJetsToLL_TuneZ2_M-50/patTuple_skim_16_0_81p.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MC/Fall11/SingleElectron/DYJetsToLL_TuneZ2_M-50/patTuple_skim_170_0_1Yd.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MC/Fall11/SingleElectron/DYJetsToLL_TuneZ2_M-50/patTuple_skim_171_0_78f.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MC/Fall11/SingleElectron/DYJetsToLL_TuneZ2_M-50/patTuple_skim_172_0_pPx.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MC/Fall11/SingleElectron/DYJetsToLL_TuneZ2_M-50/patTuple_skim_173_0_ESD.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MC/Fall11/SingleElectron/DYJetsToLL_TuneZ2_M-50/patTuple_skim_174_0_gUN.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MC/Fall11/SingleElectron/DYJetsToLL_TuneZ2_M-50/patTuple_skim_175_0_bXb.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MC/Fall11/SingleElectron/DYJetsToLL_TuneZ2_M-50/patTuple_skim_176_0_eRg.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MC/Fall11/SingleElectron/DYJetsToLL_TuneZ2_M-50/patTuple_skim_17_0_5vd.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MC/Fall11/SingleElectron/DYJetsToLL_TuneZ2_M-50/patTuple_skim_184_0_xy0.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MC/Fall11/SingleElectron/DYJetsToLL_TuneZ2_M-50/patTuple_skim_185_0_naf.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MC/Fall11/SingleElectron/DYJetsToLL_TuneZ2_M-50/patTuple_skim_186_0_SZk.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MC/Fall11/SingleElectron/DYJetsToLL_TuneZ2_M-50/patTuple_skim_187_0_oyL.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MC/Fall11/SingleElectron/DYJetsToLL_TuneZ2_M-50/patTuple_skim_188_0_M2K.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MC/Fall11/SingleElectron/DYJetsToLL_TuneZ2_M-50/patTuple_skim_189_0_VW8.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MC/Fall11/SingleElectron/DYJetsToLL_TuneZ2_M-50/patTuple_skim_18_0_snK.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MC/Fall11/SingleElectron/DYJetsToLL_TuneZ2_M-50/patTuple_skim_190_0_jb9.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MC/Fall11/SingleElectron/DYJetsToLL_TuneZ2_M-50/patTuple_skim_191_0_yR4.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MC/Fall11/SingleElectron/DYJetsToLL_TuneZ2_M-50/patTuple_skim_193_0_jmg.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MC/Fall11/SingleElectron/DYJetsToLL_TuneZ2_M-50/patTuple_skim_194_0_glW.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MC/Fall11/SingleElectron/DYJetsToLL_TuneZ2_M-50/patTuple_skim_195_0_V8q.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MC/Fall11/SingleElectron/DYJetsToLL_TuneZ2_M-50/patTuple_skim_196_0_cf7.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MC/Fall11/SingleElectron/DYJetsToLL_TuneZ2_M-50/patTuple_skim_197_0_Qss.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MC/Fall11/SingleElectron/DYJetsToLL_TuneZ2_M-50/patTuple_skim_198_0_ulp.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MC/Fall11/SingleElectron/DYJetsToLL_TuneZ2_M-50/patTuple_skim_19_0_qCk.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MC/Fall11/SingleElectron/DYJetsToLL_TuneZ2_M-50/patTuple_skim_20_0_3o5.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MC/Fall11/SingleElectron/DYJetsToLL_TuneZ2_M-50/patTuple_skim_21_0_ztQ.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MC/Fall11/SingleElectron/DYJetsToLL_TuneZ2_M-50/patTuple_skim_22_0_xz5.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MC/Fall11/SingleElectron/DYJetsToLL_TuneZ2_M-50/patTuple_skim_23_0_iE8.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MC/Fall11/SingleElectron/DYJetsToLL_TuneZ2_M-50/patTuple_skim_24_0_qnk.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MC/Fall11/SingleElectron/DYJetsToLL_TuneZ2_M-50/patTuple_skim_25_0_f5x.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MC/Fall11/SingleElectron/DYJetsToLL_TuneZ2_M-50/patTuple_skim_26_0_1bn.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MC/Fall11/SingleElectron/DYJetsToLL_TuneZ2_M-50/patTuple_skim_27_0_oAS.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MC/Fall11/SingleElectron/DYJetsToLL_TuneZ2_M-50/patTuple_skim_29_0_tiK.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MC/Fall11/SingleElectron/DYJetsToLL_TuneZ2_M-50/patTuple_skim_37_0_zBS.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MC/Fall11/SingleElectron/DYJetsToLL_TuneZ2_M-50/patTuple_skim_44_0_BbW.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MC/Fall11/SingleElectron/DYJetsToLL_TuneZ2_M-50/patTuple_skim_45_0_cBd.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MC/Fall11/SingleElectron/DYJetsToLL_TuneZ2_M-50/patTuple_skim_46_0_9Il.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MC/Fall11/SingleElectron/DYJetsToLL_TuneZ2_M-50/patTuple_skim_47_0_5ND.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MC/Fall11/SingleElectron/DYJetsToLL_TuneZ2_M-50/patTuple_skim_48_0_gis.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MC/Fall11/SingleElectron/DYJetsToLL_TuneZ2_M-50/patTuple_skim_49_0_esL.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MC/Fall11/SingleElectron/DYJetsToLL_TuneZ2_M-50/patTuple_skim_50_0_buN.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MC/Fall11/SingleElectron/DYJetsToLL_TuneZ2_M-50/patTuple_skim_51_0_53S.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MC/Fall11/SingleElectron/DYJetsToLL_TuneZ2_M-50/patTuple_skim_52_0_nDE.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MC/Fall11/SingleElectron/DYJetsToLL_TuneZ2_M-50/patTuple_skim_53_0_luQ.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MC/Fall11/SingleElectron/DYJetsToLL_TuneZ2_M-50/patTuple_skim_54_0_g2z.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MC/Fall11/SingleElectron/DYJetsToLL_TuneZ2_M-50/patTuple_skim_55_0_zbA.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MC/Fall11/SingleElectron/DYJetsToLL_TuneZ2_M-50/patTuple_skim_56_0_0Wm.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MC/Fall11/SingleElectron/DYJetsToLL_TuneZ2_M-50/patTuple_skim_57_0_lGJ.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MC/Fall11/SingleElectron/DYJetsToLL_TuneZ2_M-50/patTuple_skim_58_0_5YQ.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MC/Fall11/SingleElectron/DYJetsToLL_TuneZ2_M-50/patTuple_skim_59_0_yiH.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MC/Fall11/SingleElectron/DYJetsToLL_TuneZ2_M-50/patTuple_skim_60_0_8R6.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MC/Fall11/SingleElectron/DYJetsToLL_TuneZ2_M-50/patTuple_skim_61_0_0V6.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MC/Fall11/SingleElectron/DYJetsToLL_TuneZ2_M-50/patTuple_skim_62_0_MCQ.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MC/Fall11/SingleElectron/DYJetsToLL_TuneZ2_M-50/patTuple_skim_63_0_mpF.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MC/Fall11/SingleElectron/DYJetsToLL_TuneZ2_M-50/patTuple_skim_72_0_4ZH.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MC/Fall11/SingleElectron/DYJetsToLL_TuneZ2_M-50/patTuple_skim_73_0_qWQ.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MC/Fall11/SingleElectron/DYJetsToLL_TuneZ2_M-50/patTuple_skim_74_0_pgN.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MC/Fall11/SingleElectron/DYJetsToLL_TuneZ2_M-50/patTuple_skim_75_0_Z33.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MC/Fall11/SingleElectron/DYJetsToLL_TuneZ2_M-50/patTuple_skim_76_0_LFc.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MC/Fall11/SingleElectron/DYJetsToLL_TuneZ2_M-50/patTuple_skim_77_0_rsP.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MC/Fall11/SingleElectron/DYJetsToLL_TuneZ2_M-50/patTuple_skim_78_0_w0e.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MC/Fall11/SingleElectron/DYJetsToLL_TuneZ2_M-50/patTuple_skim_86_0_jUz.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MC/Fall11/SingleElectron/DYJetsToLL_TuneZ2_M-50/patTuple_skim_87_0_xUy.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MC/Fall11/SingleElectron/DYJetsToLL_TuneZ2_M-50/patTuple_skim_88_0_yRv.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MC/Fall11/SingleElectron/DYJetsToLL_TuneZ2_M-50/patTuple_skim_89_0_EKq.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MC/Fall11/SingleElectron/DYJetsToLL_TuneZ2_M-50/patTuple_skim_8_0_Olh.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MC/Fall11/SingleElectron/DYJetsToLL_TuneZ2_M-50/patTuple_skim_90_0_l6c.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MC/Fall11/SingleElectron/DYJetsToLL_TuneZ2_M-50/patTuple_skim_91_0_bxD.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MC/Fall11/SingleElectron/DYJetsToLL_TuneZ2_M-50/patTuple_skim_92_0_bUZ.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MC/Fall11/SingleElectron/DYJetsToLL_TuneZ2_M-50/patTuple_skim_93_0_Vsj.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MC/Fall11/SingleElectron/DYJetsToLL_TuneZ2_M-50/patTuple_skim_94_0_hVc.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MC/Fall11/SingleElectron/DYJetsToLL_TuneZ2_M-50/patTuple_skim_95_0_Dkr.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MC/Fall11/SingleElectron/DYJetsToLL_TuneZ2_M-50/patTuple_skim_96_0_tDl.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MC/Fall11/SingleElectron/DYJetsToLL_TuneZ2_M-50/patTuple_skim_97_0_5M2.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MC/Fall11/SingleElectron/DYJetsToLL_TuneZ2_M-50/patTuple_skim_98_0_clW.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MC/Fall11/SingleElectron/DYJetsToLL_TuneZ2_M-50/patTuple_skim_99_0_Rko.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MC/Fall11/SingleElectron/DYJetsToLL_TuneZ2_M-50/patTuple_skim_9_0_bJa.root',
]
        )
