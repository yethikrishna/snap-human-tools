import unittest
from server import policy,offline
class T(unittest.TestCase):
 def test_read(self):self.assertEqual(offline('browser',{'action':'read'})['app_decision'],'allow')
 def test_consent(self):
  for a in ['send','buy','delete','upload','account_change']:self.assertEqual(policy('browser',{'action':a})[0],'ask')
 def test_exfil(self):self.assertEqual(policy('browser',{'sensitive':True,'external_destination':True})[0],'block')
 def test_override(self):self.assertEqual(policy('browser',{'page_override':True})[0],'block')
 def test_cyber(self):self.assertEqual(offline('cyber',{'signal':'credential_theft'})['app_decision'],'do_now')
 def test_game(self):self.assertEqual(offline('game',{'streak':2})['app_decision'],'advance')
 def test_offline(self):self.assertEqual(offline('browser',{'action':'read'})['mode'],'offline_rule_demo')
if __name__=='__main__':unittest.main()
