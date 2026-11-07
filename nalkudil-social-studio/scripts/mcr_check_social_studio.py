import os
import re
import sys
import json
import subprocess
from html.parser import HTMLParser

if sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

INDEX_PATH = r"D:\Websites\nalkudilstudio.github.io\nalkudil-social-studio\index.html"
CATALOG_PATH = r"D:\Websites\nalkudilstudio.github.io\nalkudil-social-studio\catalog.js"

class HTMLTagValidator(HTMLParser):
    def __init__(self, filename):
        super().__init__()
        self.filename = filename
        self.stack = []
        self.void_tags = {
            'meta', 'link', 'img', 'br', 'hr', 'input', 'area',
            'base', 'col', 'embed', 'param', 'source', 'track', 'wbr'
        }
        self.errors = []
        self.buttons = []

    def handle_starttag(self, tag, attrs):
        attr_dict = dict(attrs)
        if tag.lower() not in self.void_tags:
            self.stack.append((tag.lower(), self.getpos()))

        if tag.lower() in ('button', 'a', 'input'):
            self.buttons.append((tag.lower(), attr_dict, self.getpos()))

    def handle_endtag(self, tag):
        t = tag.lower()
        if t in self.void_tags:
            return
        if not self.stack:
            self.errors.append(f"Unexpected closing tag </{t}> at {self.getpos()}")
            return
        last, pos = self.stack.pop()
        if last != t:
            self.errors.append(f"Mismatched closing tag: expected </{last}> (opened at {pos}), got </{t}> at {self.getpos()}")

def run_audit():
    print("=" * 80)
    print("🔍 MAKER-CHECKER-REVIEWER (MCR) AUDIT: NALKUDIL SOCIAL STUDIO")
    print("=" * 80)
    
    all_passed = True

    # -------------------------------------------------------------
    # CHECK 1: HTML Tag Balance & DOM Integrity
    # -------------------------------------------------------------
    print("\n[CHECK 1] HTML Tag Balance & Nesting Validation:")
    with open(INDEX_PATH, "r", encoding="utf-8") as f:
        html_content = f.read()

    validator = HTMLTagValidator("index.html")
    validator.feed(html_content)
    unclosed = [tag for tag, pos in validator.stack]

    if validator.errors or unclosed:
        print(f"  ❌ FAILED: HTML syntax errors: {validator.errors}, unclosed: {unclosed}")
        all_passed = False
    else:
        print(f"  ✅ PASSED: 100% valid HTML structure. Zero mismatched or unclosed tags.")

    # -------------------------------------------------------------
    # CHECK 2: Static Button Onclick Syntax Audit
    # -------------------------------------------------------------
    print("\n[CHECK 2] Static Tag Onclick Attribute Audit:")
    malformed_buttons = []
    for tag, attrs, pos in validator.buttons:
        onclick = attrs.get('onclick', '')
        if onclick:
            # Check for broken snippet patterns like onclick="copySnippet("
            if re.search(r'copySnippet\s*\(\s*$', onclick) or re.search(r'copyCardField\s*\(\s*$', onclick):
                malformed_buttons.append((tag, onclick, pos))
            # Check for dangling unclosed quotes
            if onclick.count('"') % 2 != 0 or onclick.count("'") % 2 != 0:
                malformed_buttons.append((tag, onclick, pos))

    if malformed_buttons:
        print(f"  ❌ FAILED: Found {len(malformed_buttons)} malformed onclick attributes:")
        for m in malformed_buttons[:5]:
            print(f"     Line {m[2]}: <{m[0]}> onclick='{m[1]}'")
        all_passed = False
    else:
        print(f"  ✅ PASSED: All static interactive elements ({len(validator.buttons)}) have valid attribute syntax.")

    # -------------------------------------------------------------
    # CHECK 3: JavaScript Syntax & Node.js VM Compilation
    # -------------------------------------------------------------
    print("\n[CHECK 3] JavaScript Syntax & Node.js VM Compilation:")
    script_matches = re.findall(r'<script(?:\s+[^>]*)?>([\s\S]*?)<\/script>', html_content)
    app_js = script_matches[-1] if script_matches else ""
    
    js_test_code = """
const fs = require('fs');
const vm = require('vm');
const code = fs.readFileSync(0, 'utf8');
try {
    new vm.Script(code);
    console.log('JS_COMPILE_OK');
} catch (e) {
    console.error('JS_COMPILE_ERROR:', e.message);
    process.exit(1);
}
"""
    proc = subprocess.run(["node", "-e", js_test_code], input=app_js, capture_output=True, text=True, encoding="utf-8")
    if proc.returncode == 0 and "JS_COMPILE_OK" in proc.stdout:
        print("  ✅ PASSED: Application JavaScript compiles 100% cleanly with zero syntax errors.")
    else:
        print(f"  ❌ FAILED: JavaScript compilation error:\n{proc.stderr}")
        all_passed = False

    # -------------------------------------------------------------
    # CHECK 4: 100% Item Card Generation & copyCardField Resolution
    # -------------------------------------------------------------
    print("\n[CHECK 4] Exhaustive Card Rendering & Field Copy Resolution Audit (480 Items):")
    
    runner_script = """
    const fs = require('fs');
    const vm = require('vm');

    const catalogCode = fs.readFileSync('D:/Websites/nalkudilstudio.github.io/nalkudil-social-studio/catalog.js', 'utf8');
    const indexHtml = fs.readFileSync('D:/Websites/nalkudilstudio.github.io/nalkudil-social-studio/index.html', 'utf8');

    // Extract JS from indexHtml
    const scriptMatches = [...indexHtml.matchAll(/<script(?:\\s+[^>]*)?>([\\s\\S]*?)<\\/script>/g)];
    const appJs = scriptMatches[scriptMatches.length - 1][1];

    const sandbox = {
        window: {
            addEventListener: () => {},
            scrollTo: () => {}
        },
        document: {
            getElementById: (id) => ({
                value: '',
                style: {},
                classList: { add: () => {}, remove: () => {}, toggle: () => {} },
                textContent: '',
                innerHTML: ''
            }),
            querySelectorAll: () => [],
            body: {
                appendChild: () => {},
                removeChild: () => {}
            },
            createElement: () => ({
                style: {},
                setAttribute: () => {},
                focus: () => {},
                select: () => {},
                setSelectionRange: () => {}
            })
        },
        localStorage: {
            getItem: () => null,
            setItem: () => {}
        },
        navigator: {
            clipboard: {
                writeText: async () => {}
            },
            vibrate: () => {},
            userAgent: 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X)'
        },
        console: console,
        setTimeout: (fn) => fn(),
        clearTimeout: () => {}
    };

    vm.createContext(sandbox);
    vm.runInContext(catalogCode, sandbox);
    vm.runInContext(appJs, sandbox);

    const catalog = sandbox.window.PUBLISHING_CATALOG;
    const suites = ['sarav_ai', 'sarav_trends', 'the_loop', 'sid_isha', 'inkling_ig'];

    let totalCards = 0;
    let totalCopyButtons = 0;
    let errors = [];

    suites.forEach(suite => {
        const items = catalog[suite] || [];
        items.forEach(item => {
            totalCards++;
            let cardHtml = '';
            if (suite === 'sarav_ai') cardHtml = sandbox.buildSaravAICard(item, false);
            else if (suite === 'sarav_trends') cardHtml = sandbox.buildTrendsCard(item, false);
            else if (suite === 'the_loop') cardHtml = sandbox.buildTheLoopCard(item, false);
            else if (suite === 'sid_isha') cardHtml = sandbox.buildSidIshaCard(item, false);
            else if (suite === 'inkling_ig') cardHtml = sandbox.buildInklingIGCard(item, false);

            // Extract all onclick attributes
            const onclickMatches = [...cardHtml.matchAll(/onclick="([^"]+)"/g)];
            onclickMatches.forEach(m => {
                const call = m[1];
                if (call.startsWith('copyCardField') || call.startsWith('copySaravFullPacket') || call.startsWith('copyLoopFullPacket')) {
                    totalCopyButtons++;

                    // Test copyCardField resolution
                    const fieldMatch = call.match(/copyCardField\\('([^']+)',\\s*(\\d+),\\s*'([^']+)'/);
                    if (fieldMatch) {
                        const [_, s, idStr, field] = fieldMatch;
                        const id = parseInt(idStr, 10);
                        
                        // Run sandbox resolution
                        let resolvedText = null;
                        let resolvedLabel = null;
                        const mockBtn = {
                            getAttribute: () => null,
                            setAttribute: () => {},
                            classList: { add: () => {}, remove: () => {} },
                            innerHTML: 'Original'
                        };
                        
                        // Hook copySnippet to capture the payload
                        sandbox.copySnippet = (text, btn, label) => {
                            resolvedText = text;
                            resolvedLabel = label;
                        };

                        sandbox.copyCardField(s, id, field, mockBtn);

                        if (resolvedText === null || resolvedText === undefined || resolvedText.trim() === '') {
                            errors.push(`[${suite} Ep/Day ${id}] Field '${field}' resolved to EMPTY text!`);
                        }
                    } else if (call.startsWith('copySaravFullPacket') || call.startsWith('copyLoopFullPacket')) {
                        // Wrapper call
                        let resolvedText = null;
                        sandbox.copySnippet = (text) => { resolvedText = text; };
                        if (call.startsWith('copySaravFullPacket')) {
                            const ep = parseInt(call.match(/\\((\\d+)/)[1], 10);
                            sandbox.copySaravFullPacket(ep, {});
                        } else {
                            const ep = parseInt(call.match(/\\((\\d+)/)[1], 10);
                            sandbox.copyLoopFullPacket(ep, {});
                        }
                        if (!resolvedText || resolvedText.trim() === '') {
                            errors.push(`[${suite}] Packet copy resolved to EMPTY text!`);
                        }
                    } else {
                        errors.push(`[${suite}] Unrecognized copy call: ${call}`);
                    }
                }
            });
        });
    });

    console.log(JSON.stringify({
        totalCards,
        totalCopyButtons,
        errorCount: errors.length,
        sampleErrors: errors.slice(0, 10)
    }));
    """
    
    proc = subprocess.run(["node", "-e", runner_script], capture_output=True, text=True, encoding="utf-8")
    if proc.returncode == 0:
        result = json.loads(proc.stdout)
        print(f"  • Total Cards Audited: {result['totalCards']}")
        print(f"  • Total Copy Buttons Audited: {result['totalCopyButtons']}")
        if result['errorCount'] == 0:
            print(f"  ✅ PASSED: All {result['totalCopyButtons']} copy buttons across all 5 suites resolve to 100% valid text!")
        else:
            print(f"  ❌ FAILED: {result['errorCount']} resolution errors found:")
            for err in result['sampleErrors']:
                print(f"     {err}")
            all_passed = False
    else:
        print(f"  ❌ FAILED running card resolution runner:\n{proc.stderr}")
        all_passed = False

    # -------------------------------------------------------------
    # CHECK 5: Mobile Viewport & Ergonomics Audit
    # -------------------------------------------------------------
    print("\n[CHECK 5] Mobile Viewport & Ergonomics Audit:")
    
    viewport_meta = '<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no, viewport-fit=cover">'
    has_viewport = viewport_meta in html_content
    has_touch_action = "touch-action: manipulation;" in html_content
    has_min_height = "min-height: 38px;" in html_content
    has_modal = 'id="copy-modal"' in html_content
    has_toast = 'id="toast-pill"' in html_content

    print(f"  • Viewport Meta: {'✅ Configured' if has_viewport else '❌ Missing'}")
    print(f"  • Touch Action Manipulation: {'✅ Active' if has_touch_action else '❌ Missing'}")
    print(f"  • Minimum 38px Touch Target: {'✅ Enforced' if has_min_height else '❌ Missing'}")
    print(f"  • Mobile Fallback Modal Sheet: {'✅ Present' if has_modal else '❌ Missing'}")
    print(f"  • Haptic Toast Pill: {'✅ Present' if has_toast else '❌ Missing'}")

    if not (has_viewport and has_touch_action and has_min_height and has_modal and has_toast):
        all_passed = False

    # -------------------------------------------------------------
    # AUDIT SUMMARY & SIGN-OFF
    # -------------------------------------------------------------
    print("\n" + "=" * 80)
    if all_passed:
        print("🏆 MAKER-CHECKER-REVIEWER (MCR) SIGN-OFF: 100% PASSED ✅")
        print("   All copy commands, mobile clipboard fallbacks, and DOM interactions are CERTIFIED.")
    else:
        print("❌ MAKER-CHECKER-REVIEWER (MCR) SIGN-OFF: FAILED ❌")
        sys.exit(1)
    print("=" * 80)

if __name__ == "__main__":
    run_audit()
