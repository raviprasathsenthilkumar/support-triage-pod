# Support Triage Pod

## Links
- App: https://support-triage-ravi.apps.lemma.work
- GitHub: https://github.com/raviprasathsenthilkumar/support-triage-pod.git

## Token Refresh
Token expires every ~1 hour. When buttons show 401, run in PowerShell then Ctrl+Shift+R:

    $token = lemma auth print-token
    $html = [System.IO.File]::ReadAllText('C:\Users\ravip\support-triage-pod\support-triage-app\index.html')
    $html = $html -replace "bearerToken='[^']*'", "bearerToken='$token'"
    [System.IO.File]::WriteAllText('C:\Users\ravip\support-triage-pod\support-triage-app\index.html', $html)
    lemma app deploy support-triage-ravi support-triage-app

## Architecture
| Layer | Detail |
|-------|--------|
| Frontend | Static HTML/CSS/JS |
| Auth | Lemma bearer token (~1hr expiry) |
| Storage | Lemma Datastore - tickets table |
| AI Triage | Lemma function: save_triage_result |
| Hosting | Lemma App: support-triage-ravi |
