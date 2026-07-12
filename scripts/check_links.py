from pathlib import Path
from datetime import datetime, timezone
import json, urllib.request, urllib.error, ssl

root = Path(__file__).resolve().parents[1]
sites = json.loads((root/'data'/'websites.json').read_text(encoding='utf-8'))
results=[]
ctx=ssl.create_default_context()
headers={'User-Agent':'Mozilla/5.0 PhD-Link-Checker/1.0'}
for site in sites:
    url=site['url']
    status=None
    ok=False
    error=''
    try:
        req=urllib.request.Request(url,headers=headers,method='GET')
        with urllib.request.urlopen(req,timeout=25,context=ctx) as r:
            status=r.status
            ok=200 <= status < 400
    except urllib.error.HTTPError as e:
        status=e.code
        # Some sites block automated requests even though they work in browsers.
        ok=e.code in (401,403,405,429)
        error=str(e)
    except Exception as e:
        error=str(e)
    results.append({'name':site['name'],'url':url,'ok':ok,'status':status,'error':error})
payload={'checked_at':datetime.now(timezone.utc).isoformat(),'results':results}
(root/'data'/'link_status.json').write_text(json.dumps(payload,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(payload,ensure_ascii=False,indent=2))
