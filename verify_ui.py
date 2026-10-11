import subprocess,time,json,os,shutil
from pathlib import Path
from playwright.sync_api import sync_playwright
root=Path(__file__).parent;s=subprocess.Popen(['python3',str(root/'server.py')],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL);time.sleep(.4)
try:
 with sync_playwright() as p:
  b=p.chromium.launch(executable_path=(os.environ.get('CHROME_BIN') or shutil.which('google-chrome') or shutil.which('chromium') or shutil.which('chromium-browser')),headless=True,args=['--no-sandbox']);page=b.new_page(viewport={'width':1440,'height':1080});page.goto('http://127.0.0.1:8775');page.wait_for_timeout(250)
  page.locator('#action').select_option('buy');page.locator('#browser-run').click();page.wait_for_timeout(250);assert page.locator('#browser-result h3').inner_text()=='ASK';page.screenshot(path=str(root/'browser-desktop.png'),full_page=True)
  page.evaluate("tab('cyber')");page.get_by_text('Route alert',exact=True).click();page.wait_for_timeout(200);assert page.locator('#cyber-result h3').inner_text()=='DO NOW';page.screenshot(path=str(root/'cyber-desktop.png'),full_page=True)
  page.evaluate("tab('game')");page.locator('#start').click();page.wait_for_function('playing===true');sequence=page.evaluate('seq');
  for n in sequence:page.locator('#pads button').nth(n).click()
  page.wait_for_function('busy===false');assert page.evaluate('wins')==1
  page.locator('#start').click();page.wait_for_function('playing===true');sequence=page.evaluate('seq');
  for n in sequence:page.locator('#pads button').nth(n).click()
  page.wait_for_function('busy===false');assert page.evaluate('level')==3;page.screenshot(path=str(root/'game-desktop.png'),full_page=True)
  page.set_viewport_size({'width':390,'height':844});page.evaluate("tab('browser')");page.screenshot(path=str(root/'browser-mobile.png'),full_page=True);assert page.evaluate('document.documentElement.scrollWidth<=390');b.close()
 (root/'ui-test-results.txt').write_text('Browser purchase -> ASK; cyber sample -> DO NOW; two actual played rounds correct -> level 3; 390px no horizontal overflow. Offline rules only; no model call.\n')
finally:s.terminate();s.wait()
