# Snap Human Tools

Three local prototypes exploring a decision model around control, attention and play.

## Run

Python 3.10+ is required. The server uses only the Python standard library.

```sh
python3 server.py
```

Open `http://127.0.0.1:8775`. Offline mode works without a key and is labeled as local rules, not Snap output.

For live mode, supply `SUBQ_API_KEY` securely in the server environment before starting it. Never put a real key in source, a browser field or a public post. Live mode submits entered evidence to SubQ and consumes credit. Use only invented or approved data. Check the provider's current data policy first.

## The three tools

- **Before the Click:** a four-step action-review sandbox. Read actions run against invented local product data. Purchases and other consequential actions remain held by application rules. Sensitive external disclosure is blocked by application rules. Model decisions are advisory, not owner permission. No real orders, sends or deletions.
- **Signal Desk:** editable sample-alert triage into do-now, watch or ignore. Live requests omit the sample's preselected signal label. These are invented alerts, not real telemetry. No scanning, confirmed threat detection or containment.
- **Pattern Run:** a playable four-pad memory game. Session outcomes guide ease, hold or advance; the app caps levels at 2-7. Steady and timed modes, round history and response timing. No human efficacy claim.

## Validation

```sh
python3 -m unittest test_tools.py
python3 -m pip install -r requirements-dev.txt
python3 -m playwright install chromium
python3 verify_ui.py
python3 verify_workflows.py
python3 verify_edgecases.py
```

UI tests use a detected Chrome/Chromium binary or Playwright's installed Chromium. Set `CHROME_BIN` to select a browser explicitly. All included checks run offline. A free local port 8775 is required.

Development validation covered seven unit tests, mobile layout, two automated correct game rounds, the four-step action plan, the four-alert queue, timed expiry and reset behavior. Seventeen live development calls tested bounded routes, not a benchmark or reliability study. Raw development receipts and private logs are deliberately excluded from this distribution. New local receipts are written to `receipts/` and ignored by Git.

## Optional current-tab extension

The `extension/` folder contains an experimental unpacked Chrome extension. Read its README before installing. It intercepts link clicks and holds form submissions only after a tab is armed. Actual loaded-extension end-to-end operation was not verified in development because service-worker startup failed. A content-script test with mocked transport is not an installed-extension test.

This is not a security boundary: pages may bypass or remove the listener, and many browser actions are outside its coverage. Do not rely on it on sensitive or dangerous sites.

## Limits

Local prototypes only. Not integrated into Nool. Not security audited. No safety guarantee, production deployment or clinical/learning benefit claim. The loopback server is not intended to be exposed on the public network. Application-enforced holds remain separate from model output.

API documentation: https://docs.subq.ai/endpoints/decisions-api/
