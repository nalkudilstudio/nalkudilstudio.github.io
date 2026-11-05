import re

html_path = r'D:\Websites\nalkudilstudio.github.io\nalkudil-social-studio\index.html'

with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Add tab button
tab_old = 'onclick="switchSuite(\'sarav_ai\', this)">\n        <span>🤖 Sarav × AI</span>\n        <span class="tab-count" id="count-sarav">100</span>\n      </button>'
tab_new = 'onclick="switchSuite(\'sarav_ai\', this)">\n        <span>🤖 Sarav × AI</span>\n        <span class="tab-count" id="count-sarav">100</span>\n      </button>\n      <button class="nav-tab-btn" onclick="switchSuite(\'sarav_trends\', this)">\n        <span>⚡ Tech Radar Trends</span>\n        <span class="tab-count" id="count-trends">6</span>\n      </button>'

if 'count-trends' not in html:
    html = html.replace('onclick="switchSuite(\'sarav_ai\', this)">\r\n        <span>🤖 Sarav × AI</span>\r\n        <span class="tab-count" id="count-sarav">100</span>\r\n      </button>', 'onclick="switchSuite(\'sarav_ai\', this)">\r\n        <span>🤖 Sarav × AI</span>\r\n        <span class="tab-count" id="count-sarav">100</span>\r\n      </button>\r\n      <button class="nav-tab-btn" onclick="switchSuite(\'sarav_trends\', this)">\r\n        <span>⚡ Tech Radar Trends</span>\r\n        <span class="tab-count" id="count-trends">6</span>\r\n      </button>')
    html = html.replace('onclick="switchSuite(\'sarav_ai\', this)">\n        <span>🤖 Sarav × AI</span>\n        <span class="tab-count" id="count-sarav">100</span>\n      </button>', 'onclick="switchSuite(\'sarav_ai\', this)">\n        <span>🤖 Sarav × AI</span>\n        <span class="tab-count" id="count-sarav">100</span>\n      </button>\n      <button class="nav-tab-btn" onclick="switchSuite(\'sarav_trends\', this)">\n        <span>⚡ Tech Radar Trends</span>\n        <span class="tab-count" id="count-trends">6</span>\n      </button>')

# 2. Add filter chips for sarav_trends
chips_marker = "if (currentSuite === 'sarav_ai') {"
chips_addition = """if (currentSuite === 'sarav_trends') {
        chips.push(
          { id: 'active', label: '🚀 Active / Live' },
          { id: 'queued', label: '⏳ Queued' }
        );
      } else if (currentSuite === 'sarav_ai') {"""
if "currentSuite === 'sarav_trends'" not in html:
    html = html.replace("if (currentSuite === 'sarav_ai') {", chips_addition)

# 3. Add filtering logic in renderCards
filter_marker = "if (currentSuite === 'sarav_ai') {"
filter_addition = """if (currentSuite === 'sarav_trends') {
          if (currentFilter === 'active' && item.status !== 'COMPLETED') return false;
          if (currentFilter === 'queued' && item.status !== 'QUEUED') return false;
        } else if (currentSuite === 'sarav_ai') {"""
# Note: we need to replace the second occurrence of "if (currentSuite === 'sarav_ai') {"
parts = html.split("if (currentSuite === 'sarav_ai') {")
if len(parts) >= 3 and "currentFilter === 'active'" not in html:
    html = parts[0] + "if (currentSuite === 'sarav_ai') {" + parts[1] + filter_addition + "if (currentSuite === 'sarav_ai') {".join(parts[2:])

# 4. Add card builder invocation
card_call_marker = "cardHtml = buildSaravAICard(item, pubSet.has(item.episode));"
card_call_addition = """cardHtml = buildSaravAICard(item, pubSet.has(item.episode));
        } else if (currentSuite === 'sarav_trends') {
          cardHtml = buildTrendsCard(item, pubSet.has(item.episode));"""
if "buildTrendsCard" not in html:
    html = html.replace(card_call_marker, card_call_addition)

# 5. Add buildTrendsCard function definition before buildSaravAICard
builder_func = """    // Builder: Sarav X AI Tech Radar Trends
    function buildTrendsCard(item, isPublished) {
      const ep = item.episode;
      const coverUrl = item.cover_url || '';
      const downloadName = item.cover_filename || `Shorts_Cover_Trend${String(ep).padStart(2, '0')}.png`;

      return `
        <article class="pub-card ${isPublished ? 'is-published' : ''}" id="card-sarav_trends-${ep}">
          <div class="card-top">
            <div class="card-meta-left">
              <span class="ep-badge" style="background: linear-gradient(135deg, #EA580C, #F97316); color: #fff;">TREND #${String(ep).padStart(2, '0')}</span>
              <span class="cat-badge">⚡ ${escapeHtml(item.day)}</span>
              <span class="cat-badge">${escapeHtml(item.category || 'Tech Radar')}</span>
              <span class="slot-badge">🕒 11:30 AM IST Daily</span>
            </div>
            <label class="status-check-label ${isPublished ? 'checked' : ''}">
              <input type="checkbox" ${isPublished ? 'checked' : ''} onchange="togglePublishStatus('sarav_trends', ${ep})">
              <span class="status-text">${isPublished ? 'Published ✅' : (item.status === 'COMPLETED' ? 'Ready 🚀' : 'Queued ⏳')}</span>
            </label>
          </div>

          <div class="card-grid">
            <div class="media-box">
              <div class="preview-thumb-wrap">
                ${coverUrl ? `<img src="${coverUrl}" alt="Trend ${ep} Cover" loading="lazy">` : `<div class="thumb-placeholder"><span>🖼️</span><span>Trend ${ep} Cover Pending</span></div>`}
              </div>
              ${coverUrl ? `<a href="${coverUrl}" download="${downloadName}" class="btn-download-direct">⬇️ Download Cover</a>` : ''}
            </div>

            <div class="content-box">
              <h2 class="card-title-text">${escapeHtml(item.title)}</h2>

              <div class="actions-grid">
                <button class="btn-copy gold" onclick="copyCardField('sarav_trends', ${ep}, 'title', this)">📋 Copy Title</button>
                <button class="btn-copy cyan" onclick="copyCardField('sarav_trends', ${ep}, 'description', this)">📋 Copy Description</button>
                <button class="btn-copy" onclick="copyCardField('sarav_trends', ${ep}, 'tags', this)">🏷️ Copy Tags</button>
                <button class="btn-copy" onclick="copyCardField('sarav_trends', ${ep}, 'pinned_comment', this)">📌 Pinned Comment</button>
              </div>

              <button class="btn-master-packet" style="background: linear-gradient(135deg, #EA580C, #F97316);" onclick="copyCardField('sarav_trends', ${ep}, 'sarav_full_packet', this)">
                ⚡ Copy Full Tech Radar Packet (Title + Desc + Tags + Pinned)
              </button>

              <details class="field-drawer">
                <summary>
                  <span>View Full Description &amp; Tags</span>
                  <span>▾</span>
                </summary>
                <div class="field-drawer-body"><b>Description:</b><br>${escapeHtml(item.description)}<br><br><b>Tags:</b><br>${escapeHtml(item.tags)}<br><br><b>Pinned Comment:</b><br>${escapeHtml(item.pinned_comment)}</div>
              </details>
            </div>
          </div>
        </article>
      `;
    }

    // Builder 1: Sarav X AI"""

if "function buildTrendsCard" not in html:
    html = html.replace("    // Builder 1: Sarav X AI", builder_func)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Updated index.html successfully!")
