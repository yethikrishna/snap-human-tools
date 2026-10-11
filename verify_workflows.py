import subprocess,time,json,os,shutil
from pathlib import Path
from playwright.sync_api import sync_playwright
root=Path(__file__).parent;s=subprocess.Popen(['python3',str(root/'server.py')],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL);time.sleep(.3)
try:
 with sync_playwright() as p:
  b=p.chromium.launch(executable_path=(os.environ.get('CHROME_BIN') or shutil.which('google-chrome') or shutil.which('chromium') or shutil.which('chromium-browser')),headless=True,args=['--no-sandbox']);page=b.new_page(viewport={'width':1920,'height':1080},device_scale_factor=2);page.goto('http://127.0.0.1:8775');page.wait_for_timeout(150)
  for i in range(4):page.locator('#plan-next').click();page.wait_for_function('(i)=>planIndex===i',arg=i+1)
  assert page.evaluate('PLAN.map(x=>x.outcome)')==['ALLOW','ALLOW','ASK','BLOCK'];assert page.evaluate('readActions')==2;page.screenshot(path=str(root/'browser-plan-complete.png'))
  page.evaluate("tab('cyber')");routes=[]
  for i in range(4):
   page.locator('#alert-queue button').nth(i).click();page.get_by_text('Route alert',exact=True).click();page.wait_for_function('(i)=>ALERTS[i].route!==undefined',arg=i);routes.append(page.evaluate('(i)=>ALERTS[i].route',i))
  assert routes==['DO_NOW','WATCH','IGNORE','DO_NOW'];page.screenshot(path=str(root/'cyber-queue-complete.png'))
  page.evaluate("tab('game')");page.locator('#focus').select_option('speed');page.locator('#start').click();page.wait_for_function('playing===true');page.wait_for_function('history.length===1',timeout=12000);assert page.evaluate('history[0].correct')==False;page.screenshot(path=str(root/'game-timed-test.png'));b.close()
 (root/'workflow-test-results.txt').write_text('Offline plan: ALLOW ALLOW ASK BLOCK; read actions=2, real orders=0. Offline cyber four-alert queue: DO_NOW WATCH IGNORE DO_NOW. Timed game unplayed round expires as miss. No API calls.\n')
finally:s.terminate();s.wait()
