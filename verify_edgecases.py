import subprocess,time
from pathlib import Path
from playwright.sync_api import sync_playwright
root=Path(__file__).parent;s=subprocess.Popen(['python3',str(root/'server.py')],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL);time.sleep(.3)
try:
 with sync_playwright() as p:
  b=p.chromium.launch(executable_path=(os.environ.get('CHROME_BIN') or shutil.which('google-chrome') or shutil.which('chromium') or shutil.which('chromium-browser')),headless=True,args=['--no-sandbox']);page=b.new_page(viewport={'width':390,'height':844});page.goto('http://127.0.0.1:8775');page.wait_for_timeout(150)
  for tab in ['browser','cyber','game']:
   page.evaluate('(k)=>window.tab(k)',tab);assert page.evaluate('document.documentElement.scrollWidth<=390')
  page.evaluate("tab('game')");page.locator('#start').click();page.wait_for_timeout(350);page.locator('button').filter(has_text='Reset session').click();page.wait_for_timeout(2000);assert page.evaluate('playing===false&&busy===false&&history.length===0')
  page.evaluate("tab('cyber')");page.locator('#alert').fill('<img src=x onerror=alert(1)>');page.get_by_text('Route alert',exact=True).click();page.wait_for_timeout(120);assert page.locator('#cyber-result img').count()==0
  page.evaluate("tab('browser')");page.locator('#plan-next').click();page.wait_for_function('planIndex===1');assert page.evaluate('readActions')==1
  page.locator('#plan-next').click();page.wait_for_function('planIndex===2');assert page.evaluate('readActions')==2
  page.locator('#plan-next').click();page.wait_for_function('planIndex===3');assert page.evaluate('readActions')==2
  with page.expect_download() as d:page.locator('#browser-result').get_by_text('Download receipt',exact=True).click()
  assert d.value.suggested_filename=='browser-receipt.json';b.close()
 (root/'edge-test-results.txt').write_text('390px all workspaces no overflow; mid-sequence reset cancels game; text rendered inert; only two reads execute in plan; ASK does not execute; receipt download succeeds. Offline only.\n')
finally:s.terminate();s.wait()
