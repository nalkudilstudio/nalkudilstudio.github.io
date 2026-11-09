"""
Patch index.html to add Comic Tales tab and functionality.
"""
import re

INDEX_PATH = r"D:\Websites\nalkudilstudio.github.io\nalkudil-social-studio\index.html"

with open(INDEX_PATH, "r", encoding="utf-8") as f:
    html = f.read()

# 1. Add Navigation Tab
nav_target = """      <button class="nav-tab-btn" onclick="switchSuite('the_loop', this)">
        <span>🔁 The Loop</span>
        <span class="tab-count" id="count-loop">300</span>
      </button>"""

nav_replacement = """      <button class="nav-tab-btn" onclick="switchSuite('the_loop', this)">
        <span>🔁 The Loop</span>
        <span class="tab-count" id="count-loop">300</span>
      </button>
      <button class="nav-tab-btn" onclick="switchSuite('comic_tales', this)">
        <span>⚖️ Comic Tales</span>
        <span class="tab-count" id="count-comic">50</span>
      </button>"""

if nav_target not in html:
    raise ValueError("nav_target not found in index.html")
html = html.replace(nav_target, nav_replacement)

# 2. Add storageKeys
storage_target = """    const storageKeys = {
      sarav_ai: 'nss_published_sarav_ai',
      the_loop: 'nss_published_the_loop',
      sid_isha: 'nss_published_sid_isha',
      inkling_ig: 'nss_published_inkling_ig'
    };"""

storage_replacement = """    const storageKeys = {
      sarav_ai: 'nss_published_sarav_ai',
      the_loop: 'nss_published_the_loop',
      sid_isha: 'nss_published_sid_isha',
      inkling_ig: 'nss_published_inkling_ig',
      sarav_trends: 'nss_published_sarav_trends',
      comic_tales: 'nss_published_comic_tales'
    };"""

if storage_target not in html:
    raise ValueError("storage_target not found in index.html")
html = html.replace(storage_target, storage_replacement)

# 3. Add togglePublishStatus text handler
toggle_target = """          if (suite === 'sarav_trends') {
            const trItem = (catalog.sarav_trends || []).find(x => x.episode === id);
            checkLabel.querySelector('.status-text').textContent = isPub ? 'Published ✅' : (trItem && trItem.status === 'COMPLETED' ? 'Ready 🚀' : 'Queued ⏳');
          } else {
            checkLabel.querySelector('.status-text').textContent = isPub ? 'Published ✅' : 'Pending';
          }"""

toggle_replacement = """          if (suite === 'sarav_trends') {
            const trItem = (catalog.sarav_trends || []).find(x => x.episode === id);
            checkLabel.querySelector('.status-text').textContent = isPub ? 'Published ✅' : (trItem && trItem.status === 'COMPLETED' ? 'Ready 🚀' : 'Queued ⏳');
          } else if (suite === 'comic_tales') {
            const ctItem = (catalog.comic_tales || []).find(x => x.episode === id);
            checkLabel.querySelector('.status-text').textContent = isPub ? 'Published ✅' : (ctItem && ctItem.status === 'READY 🚀' ? 'Ready 🚀' : 'Queued ⏳');
          } else {
            checkLabel.querySelector('.status-text').textContent = isPub ? 'Published ✅' : 'Pending';
          }"""

if toggle_target not in html:
    raise ValueError("toggle_target not found in index.html")
html = html.replace(toggle_target, toggle_replacement)

# 4. Add filter chips for comic_tales
chips_target = """      } else if (currentSuite === 'inkling_ig') {
        chips.push(
          { id: 'cat_memory', label: 'Memory' },
          { id: 'cat_twist', label: 'Twist' },
          { id: 'cat_love', label: 'Love' },
          { id: 'cat_scifi', label: 'Sci-Fi' },
          { id: 'cat_hope', label: 'Hope' },
          { id: 'pending', label: '⏳ Pending' },
          { id: 'published', label: '✅ Published' }
        );
      }"""

chips_replacement = """      } else if (currentSuite === 'inkling_ig') {
        chips.push(
          { id: 'cat_memory', label: 'Memory' },
          { id: 'cat_twist', label: 'Twist' },
          { id: 'cat_love', label: 'Love' },
          { id: 'cat_scifi', label: 'Sci-Fi' },
          { id: 'cat_hope', label: 'Hope' },
          { id: 'pending', label: '⏳ Pending' },
          { id: 'published', label: '✅ Published' }
        );
      } else if (currentSuite === 'comic_tales') {
        chips.push(
          { id: 'all', label: 'All (50)' },
          { id: 'ready', label: '🚀 Ready (5)' },
          { id: 'cat_traffic', label: '🚗 Traffic & Road' },
          { id: 'cat_digital', label: '📱 Digital & Social' },
          { id: 'cat_office', label: '💼 Corporate & Office' },
          { id: 'cat_civic', label: '🌱 Civic Sense' },
          { id: 'cat_daily', label: '🏡 Neighbors & Life' },
          { id: 'pending', label: '⏳ Pending' },
          { id: 'published', label: '✅ Published' }
        );
      }"""

if chips_target not in html:
    raise ValueError("chips_target not found in index.html")
html = html.replace(chips_target, chips_replacement)

# 5. Add filtering logic in renderCards
filter_logic_target = """        } else if (currentSuite === 'inkling_ig') {
          const cat = (item.category || '').toLowerCase();
          if (currentFilter === 'cat_memory' && !cat.includes('memory')) return false;
          if (currentFilter === 'cat_twist' && !cat.includes('twist')) return false;
          if (currentFilter === 'cat_love' && !cat.includes('love')) return false;
          if (currentFilter === 'cat_scifi' && !cat.includes('sci')) return false;
          if (currentFilter === 'cat_hope' && !cat.includes('hope')) return false;
        }"""

filter_logic_replacement = """        } else if (currentSuite === 'inkling_ig') {
          const cat = (item.category || '').toLowerCase();
          if (currentFilter === 'cat_memory' && !cat.includes('memory')) return false;
          if (currentFilter === 'cat_twist' && !cat.includes('twist')) return false;
          if (currentFilter === 'cat_love' && !cat.includes('love')) return false;
          if (currentFilter === 'cat_scifi' && !cat.includes('sci')) return false;
          if (currentFilter === 'cat_hope' && !cat.includes('hope')) return false;
        } else if (currentSuite === 'comic_tales') {
          const cat = item.category || '';
          if (currentFilter === 'ready' && item.status !== 'READY 🚀') return false;
          if (currentFilter === 'cat_traffic' && !cat.includes('போக்குவரத்து')) return false;
          if (currentFilter === 'cat_digital' && !cat.includes('டிஜிட்டல்')) return false;
          if (currentFilter === 'cat_office' && !cat.includes('அலுவலக')) return false;
          if (currentFilter === 'cat_civic' && !cat.includes('சமூக விழிப்புணர்வு')) return false;
          if (currentFilter === 'cat_daily' && !cat.includes('அண்டைவீட்டார்')) return false;
        }"""

if filter_logic_target not in html:
    raise ValueError("filter_logic_target not found in index.html")
html = html.replace(filter_logic_target, filter_logic_replacement)

# 6. Add card build dispatch in renderCards
dispatch_target = """        } else if (currentSuite === 'inkling_ig') {
          cardHtml = buildInklingIGCard(item, pubSet.has(item.episode));
        }"""

dispatch_replacement = """        } else if (currentSuite === 'inkling_ig') {
          cardHtml = buildInklingIGCard(item, pubSet.has(item.episode));
        } else if (currentSuite === 'comic_tales') {
          cardHtml = buildComicTalesCard(item, pubSet.has(item.episode));
        }"""

if dispatch_target not in html:
    raise ValueError("dispatch_target not found in index.html")
html = html.replace(dispatch_target, dispatch_replacement)

# 7. Add buildComicTalesCard builder function
builder_func = """
    // Builder 5: Comic Tales / Karma Strikes
    function buildComicTalesCard(item, isPublished) {
      const ep = item.episode;
      const coverUrl = item.cover_url || '';
      const downloadName = item.cover_filename || `cover_comic_${String(ep).padStart(3, '0')}.jpg`;
      const isReady = item.status === 'READY 🚀';

      return `
        <article class="pub-card ${isPublished ? 'is-published' : ''}" id="card-comic_tales-${ep}">
          <div class="card-top">
            <div class="card-meta-left">
              <span class="ep-badge gold" style="background: linear-gradient(135deg, #E6C875, #B89230); color: #070B11; font-weight: 800;">EP #${String(ep).padStart(2, '0')}</span>
              <span class="cat-badge" style="background: rgba(230, 200, 117, 0.12); color: var(--gold-bright); border: 1px solid rgba(230, 200, 117, 0.3);">${escapeHtml(item.category)}</span>
              <span class="cat-badge">🏛️ Melogam Justice</span>
              <span class="slot-badge">🕒 13:30 IST Lunchtime Drop</span>
            </div>
            <label class="status-check-label ${isPublished ? 'checked' : ''}">
              <input type="checkbox" ${isPublished ? 'checked' : ''} onchange="togglePublishStatus('comic_tales', ${ep})">
              <span class="status-text">${isPublished ? 'Published ✅' : (isReady ? 'Ready 🚀' : 'Queued ⏳')}</span>
            </label>
          </div>

          <div class="card-grid">
            <div class="media-box">
              <div class="preview-thumb-wrap">
                ${coverUrl ? `<img src="${coverUrl}" alt="Ep ${ep} Cover" loading="lazy">` : `<div class="thumb-placeholder"><span>⚖️</span><span>Comic Tale ${ep}</span></div>`}
              </div>
              ${coverUrl ? `<a href="${coverUrl}" download="${downloadName}" class="btn-download-direct">⬇️ Download Shorts Cover</a>` : ''}
              ${isReady ? `<div style="margin-top: 6px; text-align: center; font-size: 11px; color: var(--green); font-weight: 700;">✅ Master V4 Cut Ready</div>` : `<div style="margin-top: 6px; text-align: center; font-size: 11px; color: var(--amber); font-weight: 600;">⏳ Dialogue Staged</div>`}
            </div>

            <div class="content-box">
              <!-- Dialogue Spotlight -->
              <div style="background: rgba(7, 11, 17, 0.85); border: 1px solid rgba(255, 255, 255, 0.08); border-radius: 10px; padding: 10px 12px; margin-bottom: 8px;">
                <div style="font-size: 12px; color: var(--teal); font-weight: 700; margin-bottom: 4px;">🗣️ பூலோகம் (மனிதன்):</div>
                <div style="font-size: 13px; color: #E2E8F0; line-height: 1.4; margin-bottom: 8px; font-style: italic;">"${escapeHtml(item.human_complaint || '')}"</div>
                <div style="font-size: 12px; color: var(--gold-bright); font-weight: 700; margin-bottom: 4px;">⚡ மேலோகம் (கடவுளின் தீர்ப்பு):</div>
                <div style="font-size: 13px; color: #FFF; line-height: 1.4; font-weight: 600;">"${escapeHtml(item.divine_verdict || '')}"</div>
              </div>

              <h2 class="card-title-text">${escapeHtml(item.title)}</h2>

              <div class="actions-grid">
                <button class="btn-copy gold" onclick="copyCardField('comic_tales', ${ep}, 'title', this)">📋 Copy Title</button>
                <button class="btn-copy cyan" onclick="copyCardField('comic_tales', ${ep}, 'description', this)">📋 Copy Description</button>
                <button class="btn-copy" onclick="copyCardField('comic_tales', ${ep}, 'tags', this)">🏷️ Copy Tags</button>
                <button class="btn-copy" onclick="copyCardField('comic_tales', ${ep}, 'pinned_comment', this)">📌 Pinned Comment</button>
                <button class="btn-copy magenta" onclick="copyCardField('comic_tales', ${ep}, 'tamil_dialogue', this)">🗣️ Copy Dialogue</button>
              </div>

              <button class="btn-master-packet" style="background: linear-gradient(135deg, rgba(230, 200, 117, 0.28), rgba(0, 240, 255, 0.2)); border-color: var(--gold);" onclick="copyCardField('comic_tales', ${ep}, 'comic_full_packet', this)">
                ⚡ Copy Full Karma Shorts Packet (Title + Desc + Tags + Pinned)
              </button>

              <details class="field-drawer">
                <summary>
                  <span>View Full Description &amp; Tags</span>
                  <span>▾</span>
                </summary>
                <div class="field-drawer-body">
                  <b>YouTube Shorts Title:</b><br>${escapeHtml(item.title)}<br><br>
                  <b>Description:</b><br>${escapeHtml(item.description)}<br><br>
                  <b>Tags:</b><br>${escapeHtml(item.tags)}<br><br>
                  <b>Pinned Comment:</b><br>${escapeHtml(item.pinned_comment)}
                </div>
              </details>
            </div>
          </div>
        </article>
      `;
    }
"""

# Place buildComicTalesCard right after buildInklingIGCard
builder_insert_target = "    // Universal Master Field Copy Helper"
if builder_insert_target not in html:
    raise ValueError("builder_insert_target not found in index.html")
html = html.replace(builder_insert_target, builder_func + "\n    // Universal Master Field Copy Helper")

# 8. Add copyCardField cases
copy_case_target = """        case 'alt_text':
          text = item.alt_text || '';
          label = 'Alt Text';
          break;"""

copy_case_replacement = """        case 'alt_text':
          text = item.alt_text || '';
          label = 'Alt Text';
          break;
        case 'comic_full_packet':
          text = `TITLE:\\n${item.title || ''}\\n\\nDESCRIPTION:\\n${item.description || ''}\\n\\nTAGS:\\n${item.tags || ''}\\n\\nPINNED COMMENT:\\n${item.pinned_comment || ''}`;
          label = 'Full Karma Shorts Packet';
          break;
        case 'tamil_dialogue':
          text = `🗣️ பூலோகம் / மனிதன்:\\n"${item.human_complaint || ''}"\\n\\n⚡ மேலோகம் / கடவுளின் தீர்ப்பு:\\n"${item.divine_verdict || ''}"`;
          label = 'Tamil Dialogue';
          break;"""

if copy_case_target not in html:
    raise ValueError("copy_case_target not found in index.html")
html = html.replace(copy_case_target, copy_case_replacement)

# 9. Update DOMContentLoaded counts
dom_target = """    window.addEventListener('DOMContentLoaded', () => {
      renderFilterChips();
      renderCards();
      updatePublishedCount();
    });"""

dom_replacement = """    window.addEventListener('DOMContentLoaded', () => {
      if (document.getElementById('count-sarav')) document.getElementById('count-sarav').textContent = (catalog.sarav_ai || []).length;
      if (document.getElementById('count-trends')) document.getElementById('count-trends').textContent = (catalog.sarav_trends || []).length;
      if (document.getElementById('count-loop')) document.getElementById('count-loop').textContent = (catalog.the_loop || []).length;
      if (document.getElementById('count-comic')) document.getElementById('count-comic').textContent = (catalog.comic_tales || []).length;
      if (document.getElementById('count-sidisha')) document.getElementById('count-sidisha').textContent = (catalog.sid_isha || []).length;
      if (document.getElementById('count-inkling')) document.getElementById('count-inkling').textContent = (catalog.inkling_ig || []).length;

      renderFilterChips();
      renderCards();
      updatePublishedCount();
    });"""

if dom_target not in html:
    raise ValueError("dom_target not found in index.html")
html = html.replace(dom_target, dom_replacement)

with open(INDEX_PATH, "w", encoding="utf-8") as f:
    f.write(html)

print("index.html successfully patched with Comic Tales tab & cards!")
