Before the Click Chrome extension prototype

This extends the isolated demo into an actual current-tab link/form interception workflow. Not installed in the user's browser. Requires their manual choice to install/arm. Not Nool integration.

Load unpacked extension folder at chrome://extensions in developer mode. Copy its installed ID. Start the local server with SNAP_EXTENSION_ORIGIN=chrome-extension://THE_EXACT_ID and optionally SUBQ_API_KEY securely in the environment. Local server rejects all other extension origins.

Click extension -> write page task -> arm current tab. Clicking a link displays a held-action panel. Local review makes no Snap call. Explicit live review confirms which page metadata is submitted and consumes credit. Even ALLOW still needs a click on "I choose to open this link". Form submission never proceeds in this prototype. No form values or full page content collected. Page title/link label/URL may themselves contain private data: do not use live mode on sensitive sites.

Limitations: early prototype, not security audited. Does not cover programmatic navigation, all iframe actions, SPA-specific click effects, downloads, clipboard, network requests or every browser event. Capture listener is not a secure sandbox. Malicious pages can bypass/remove it. No claim of guaranteed protection. Use isolated test pages first, never rely on it for a dangerous site. Chrome activeTab+scripting gives access only after you explicitly arm a tab; localhost host permission connects the local review server.
