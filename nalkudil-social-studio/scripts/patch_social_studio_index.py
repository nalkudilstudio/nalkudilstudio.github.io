import re

INDEX_PATH = r"D:\Websites\nalkudilstudio.github.io\nalkudil-social-studio\index.html"

with open(INDEX_PATH, "r", encoding="utf-8") as f:
    html = f.read()

# 1. Update Tabs Nav: Add Playlists Hub tab
nav_old = """      <button class="nav-tab-btn" onclick="switchSuite('inkling_ig', this)">
        <span>✦ Inkling IG</span>
        <span class="tab-count" id="count-inkling">50</span>
      </button>"""

nav_new = """      <button class="nav-tab-btn" onclick="switchSuite('inkling_ig', this)">
        <span>✦ Inkling IG</span>
        <span class="tab-count" id="count-inkling">50</span>
      </button>
      <button class="nav-tab-btn" onclick="switchSuite('sarav_playlists', this)">
        <span>📺 Playlists Hub</span>
        <span class="tab-count" id="count-playlists">11</span>
      </button>"""

assert nav_old in html, "Tabs nav target not found"
html = html.replace(nav_old, nav_new, 1)
print("1. Added Playlists Hub tab to navigation.")

# 2. Update renderFilterChips: Add chips for sarav_playlists and update sarav_ai to include c5
chips_target = """      } else if (currentSuite === 'sarav_ai') {
        chips.push(
          { id: 'c1', label: 'Cluster 1: LLMs (1–10)' },
          { id: 'c2', label: 'Cluster 2: Prompting (11–20)' },
          { id: 'c3', label: 'Cluster 3: RAG (21–30)' },
          { id: 'c4', label: 'Cluster 4: Agents (31–40)' },
          { id: 'upcoming', label: 'Upcoming (41–100)' },
          { id: 'pending', label: '⏳ Pending' },
          { id: 'published', label: '✅ Published' }
        );"""

chips_replacement = """      } else if (currentSuite === 'sarav_ai') {
        chips.push(
          { id: 'c1', label: 'Cluster 1: LLMs (1–10)' },
          { id: 'c2', label: 'Cluster 2: Prompting (11–20)' },
          { id: 'c3', label: 'Cluster 3: RAG (21–30)' },
          { id: 'c4', label: 'Cluster 4: Agents (31–40)' },
          { id: 'c5', label: 'Cluster 5: GenAI (41–50)' },
          { id: 'upcoming', label: 'Upcoming (51–100)' },
          { id: 'pending', label: '⏳ Pending' },
          { id: 'published', label: '✅ Published' }
        );
      } else if (currentSuite === 'sarav_playlists') {
        chips.push(
          { id: 'clusters', label: 'All 10 Clusters' },
          { id: 'c5to10', label: 'Clusters 5–10 (New)' },
          { id: 'master', label: 'Master Umbrella' }
        );"""

assert chips_target in html, "Chips target not found"
html = html.replace(chips_target, chips_replacement, 1)
print("2. Updated filter chips for Sarav AI & Playlists.")

# 3. Update renderCards: Add sarav_playlists filtering and card dispatch
render_cards_filter_target = """        } else if (currentSuite === 'sarav_ai') {
          const ep = item.episode;
          if (currentFilter === 'c1' && !(ep >= 1 && ep <= 10)) return false;
          if (currentFilter === 'c2' && !(ep >= 11 && ep <= 20)) return false;
          if (currentFilter === 'c3' && !(ep >= 21 && ep <= 30)) return false;
          if (currentFilter === 'c4' && !(ep >= 31 && ep <= 40)) return false;
          if (currentFilter === 'upcoming' && !(ep >= 41)) return false;"""

render_cards_filter_replacement = """        } else if (currentSuite === 'sarav_ai') {
          const ep = item.episode;
          if (currentFilter === 'c1' && !(ep >= 1 && ep <= 10)) return false;
          if (currentFilter === 'c2' && !(ep >= 11 && ep <= 20)) return false;
          if (currentFilter === 'c3' && !(ep >= 21 && ep <= 30)) return false;
          if (currentFilter === 'c4' && !(ep >= 31 && ep <= 40)) return false;
          if (currentFilter === 'c5' && !(ep >= 41 && ep <= 50)) return false;
          if (currentFilter === 'upcoming' && !(ep >= 51)) return false;
        } else if (currentSuite === 'sarav_playlists') {
          if (currentFilter === 'c5to10' && (item.cluster_num < 5 || item.cluster_num > 10)) return false;
          if (currentFilter === 'clusters' && item.cluster_num === 0) return false;
          if (currentFilter === 'master' && item.cluster_num !== 0) return false;"""

assert render_cards_filter_target in html, "renderCards filter target not found"
html = html.replace(render_cards_filter_target, render_cards_filter_replacement, 1)

render_dispatch_target = """        } else if (currentSuite === 'comic_tales') {
          cardHtml = buildComicTalesCard(item, pubSet.has(item.episode));
        }"""

render_dispatch_replacement = """        } else if (currentSuite === 'comic_tales') {
          cardHtml = buildComicTalesCard(item, pubSet.has(item.episode));
        } else if (currentSuite === 'sarav_playlists') {
          cardHtml = buildPlaylistsCard(item);
        }"""

assert render_dispatch_target in html, "render dispatch target not found"
html = html.replace(render_dispatch_target, render_dispatch_replacement, 1)
print("3. Updated renderCards dispatch.")

# 4. Replace buildSaravAICard with enhanced individual option copy buttons and WhatsApp post
old_builder_pattern = re.compile(r"    // Builder 1: Sarav X AI\s+function buildSaravAICard\(item, isPublished\) \{[\s\S]*?    \}\s+    // Builder 2: The Loop", re.MULTILINE)

new_builder_code = """    // Builder 1: Sarav X AI
    function buildSaravAICard(item, isPublished) {
      const ep = item.episode;
      const coverUrl = item.cover_url || '';
      const poll = item.poll || {};
      const downloadName = item.cover_filename || `Sarav_AI_Shorts_Ep${String(ep).padStart(3, '0')}_Cover.png`;

      const pollOptsHtml = (poll.options || []).map((opt, i) => {
        const isCorrect = i === poll.correct_index;
        const optChar = String.fromCharCode(65 + i);
        const charCount = opt.length;
        const isTooLong = charCount > 80;
        return `
          <div class="poll-opt-item ${isCorrect ? 'correct' : ''}" style="display: flex; justify-content: space-between; align-items: center; gap: 8px; margin-bottom: 4px; padding: 6px 10px;">
            <span style="flex: 1; line-height: 1.35;">
              <b>${optChar})</b> ${escapeHtml(opt)} 
              ${isCorrect ? '<span style="color: #10B981; font-weight: 700; margin-left: 4px;">✓ (Key)</span>' : ''}
              <span style="font-size: 10px; color: ${isTooLong ? '#EF4444' : '#64748B'}; margin-left: 6px; font-weight: 500;">(${charCount}/80 chars)</span>
            </span>
            <button class="btn-copy" style="padding: 3px 8px; font-size: 11px; min-height: 26px; white-space: nowrap;" onclick="copyCardField('sarav_ai', ${ep}, 'poll_opt_${i}', this)">
              📋 Copy ${optChar}
            </button>
          </div>
        `;
      }).join('');

      return `
        <article class="pub-card ${isPublished ? 'is-published' : ''}" id="card-sarav_ai-${ep}">
          <div class="card-top">
            <div class="card-meta-left">
              <span class="ep-badge">EP #${String(ep).padStart(3, '0')}</span>
              <span class="cat-badge">${escapeHtml(item.day)}</span>
              <span class="cat-badge">${escapeHtml(item.category)}</span>
              <span class="slot-badge">🕒 18:00 IST Daily</span>
              ${item.youtube_url ? `<a href="${item.youtube_url}" target="_blank" rel="noopener" class="cat-badge" style="background: rgba(239, 68, 68, 0.2); color: #EF4444; border: 1px solid rgba(239, 68, 68, 0.4); text-decoration: none;">▶️ Live Short</a>` : ''}
            </div>
            <label class="status-check-label ${isPublished ? 'checked' : ''}">
              <input type="checkbox" ${isPublished ? 'checked' : ''} onchange="togglePublishStatus('sarav_ai', ${ep})">
              <span class="status-text">${isPublished ? 'Published ✅' : 'Pending'}</span>
            </label>
          </div>

          <div class="card-grid">
            <div class="media-box">
              <div class="preview-thumb-wrap">
                ${coverUrl ? `<img src="${coverUrl}" alt="Ep ${ep} Cover" loading="lazy">` : `<div class="thumb-placeholder"><span>🖼️</span><span>Ep ${ep} Cover Pending</span></div>`}
              </div>
              ${coverUrl ? `<a href="${coverUrl}" download="${downloadName}" class="btn-download-direct">⬇️ Download Cover</a>` : ''}
            </div>

            <div class="content-box">
              <h2 class="card-title-text">${escapeHtml(item.title)}</h2>

              <!-- Quick Copy Action Suite -->
              <div class="actions-grid">
                <button class="btn-copy gold" onclick="copyCardField('sarav_ai', ${ep}, 'title', this)">📋 Copy Title</button>
                <button class="btn-copy cyan" onclick="copyCardField('sarav_ai', ${ep}, 'description', this)">📋 Copy Description</button>
                <button class="btn-copy" onclick="copyCardField('sarav_ai', ${ep}, 'tags', this)">🏷️ Copy Tags</button>
                <button class="btn-copy" onclick="copyCardField('sarav_ai', ${ep}, 'pinned_comment', this)">📌 Pinned Comment</button>
              </div>

              <!-- Master Packet Button -->
              <button class="btn-master-packet" onclick="copyCardField('sarav_ai', ${ep}, 'sarav_full_packet', this)">
                ⚡ Copy Full YouTube Shorts Packet (Title + Desc + Tags + Pinned)
              </button>

              <!-- WhatsApp Broadcast Post Section -->
              <div class="whatsapp-box" style="background: rgba(37, 211, 102, 0.08); border: 1px solid rgba(37, 211, 102, 0.3); border-radius: 12px; padding: 12px; margin-top: 8px;">
                <div style="display: flex; justify-content: space-between; align-items: center; gap: 8px;">
                  <span style="font-family: 'Outfit', sans-serif; font-size: 12px; font-weight: 800; color: #25D366; text-transform: uppercase; letter-spacing: 0.5px; display: flex; align-items: center; gap: 6px;">
                    📱 WhatsApp Channel Broadcast
                  </span>
                  <button class="btn-copy" style="background: #25D366; color: #070B11; font-weight: 700; font-size: 11px; padding: 5px 12px; border: none;" onclick="copyCardField('sarav_ai', ${ep}, 'whatsapp_post', this)">
                    💬 Copy WhatsApp Post
                  </button>
                </div>
                <details class="field-drawer" style="margin-top: 6px; border: none; background: transparent;">
                  <summary style="font-size: 11px; color: #94A3B8; padding: 4px 0;">
                    <span>Preview Broadcast Message</span>
                    <span>▾</span>
                  </summary>
                  <div class="field-drawer-body" style="white-space: pre-wrap; font-family: 'JetBrains Mono', monospace; font-size: 11px; background: rgba(5, 15, 10, 0.7); border: 1px solid rgba(37, 211, 102, 0.2); border-radius: 6px; padding: 8px; margin-top: 4px; color: #E2E8F0;">${escapeHtml(item.whatsapp_post || '')}</div>
                </details>
              </div>

              <!-- Community Poll Section with 1-Click Option Buttons -->
              <div class="poll-box" style="margin-top: 8px;">
                <div class="poll-header">
                  <span class="poll-title">🗳️ YouTube Community Poll (≤ 80 Chars / Option)</span>
                  <button class="btn-copy cyan" style="padding: 4px 10px; font-size: 11px;" onclick="copyCardField('sarav_ai', ${ep}, 'poll_full', this)">📋 Copy Full Poll</button>
                </div>
                <p class="poll-question-text" style="font-size: 13.5px; line-height: 1.45; margin: 4px 0;">${escapeHtml(poll.question || '')}</p>
                <div class="poll-options-list">
                  ${pollOptsHtml}
                </div>
                <div class="poll-actions-row" style="margin-top: 8px; display: flex; gap: 8px; flex-wrap: wrap;">
                  <button class="btn-copy gold" style="font-size: 11.5px; padding: 6px 12px;" onclick="copyCardField('sarav_ai', ${ep}, 'poll_question', this)">📋 Copy Question Only</button>
                  <button class="btn-copy" style="font-size: 11.5px; padding: 6px 12px;" onclick="copyCardField('sarav_ai', ${ep}, 'poll_options', this)">📋 Copy All Options (A-D)</button>
                </div>
              </div>

              <!-- Expandable Description & Details -->
              <details class="field-drawer" style="margin-top: 8px;">
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

    // Builder 2: The Loop"""

assert old_builder_pattern.search(html), "Old buildSaravAICard pattern not found"
html = old_builder_pattern.sub(new_builder_code, html, count=1)
print("4. Replaced buildSaravAICard with enhanced poll options & WhatsApp broadcast.")

# 5. Add buildPlaylistsCard & copyPlaylistField
playlist_builder_code = """
    // Builder: YouTube Playlists Hub
    function buildPlaylistsCard(item) {
      const isMaster = item.cluster_num === 0;
      return `
        <article class="pub-card" id="card-playlist-${item.id}">
          <div class="card-top">
            <div class="card-meta-left">
              <span class="ep-badge ${isMaster ? 'magenta' : 'gold'}">${isMaster ? 'MASTER SERIES' : 'CLUSTER ' + item.cluster_num}</span>
              <span class="cat-badge">${escapeHtml(item.episodes_range)}</span>
              <span class="cat-badge">${escapeHtml(item.cluster_title)}</span>
              ${item.playlist_url ? `<a href="${item.playlist_url}" target="_blank" rel="noopener" class="cat-badge" style="background: rgba(239, 68, 68, 0.2); color: #EF4444; border: 1px solid rgba(239, 68, 68, 0.4); text-decoration: none;">▶️ Open on YouTube</a>` : ''}
            </div>
          </div>
          <div class="content-box" style="padding: 16px;">
            <h2 class="card-title-text" style="font-size: 16px; margin-bottom: 12px; line-height: 1.4;">${escapeHtml(item.title)}</h2>
            <div class="actions-grid" style="margin-bottom: 10px;">
              <button class="btn-copy gold" onclick="copyPlaylistField('${item.id}', 'title', this)">📋 Copy Playlist Title</button>
              <button class="btn-copy cyan" onclick="copyPlaylistField('${item.id}', 'description', this)">📋 Copy Description</button>
              <button class="btn-copy" onclick="copyPlaylistField('${item.id}', 'hashtags', this)">🏷️ Copy Hashtags</button>
            </div>
            <button class="btn-master-packet" onclick="copyPlaylistField('${item.id}', 'full_packet', this)" style="margin-bottom: 12px;">
              ⚡ Copy Full Playlist Setup Packet (Title + Description)
            </button>
            <details class="field-drawer" open>
              <summary><span>View Complete SEO Description &amp; 10-Episode Curriculum</span><span>▾</span></summary>
              <div class="field-drawer-body" style="white-space: pre-wrap; font-family: 'JetBrains Mono', monospace; font-size: 11.5px; line-height: 1.5; color: #E2E8F0;">${escapeHtml(item.description)}</div>
            </details>
          </div>
        </article>
      `;
    }

    function copyPlaylistField(id, field, btn) {
      const list = catalog.sarav_playlists || [];
      const item = list.find(x => x.id === id);
      if (!item) return showToast('⚠️ Playlist not found.');
      let text = '';
      let label = 'Playlist Field';
      if (field === 'title') {
        text = item.title;
        label = 'Playlist Title';
      } else if (field === 'description') {
        text = item.description;
        label = 'Playlist Description';
      } else if (field === 'hashtags') {
        text = item.hashtags;
        label = 'Hashtags';
      } else if (field === 'full_packet') {
        text = `PLAYLIST TITLE:\n${item.title}\n\nPLAYLIST DESCRIPTION:\n${item.description}`;
        label = 'Full Playlist Setup Packet';
      }
      copySnippet(text, btn, label);
    }
"""

# Place it before copyCardField
copy_target = "    function copyCardField(suite, id, field, btnElement) {"
assert copy_target in html, "copyCardField target not found"
html = html.replace(copy_target, playlist_builder_code + "\n" + copy_target, 1)
print("5. Added buildPlaylistsCard & copyPlaylistField.")

# 6. Update copyCardField switch statement to handle poll_opt_0..3 and whatsapp_post
switch_target = """        case 'poll_options':
          text = (item.poll && item.poll.options) ? item.poll.options.join('\\n') : '';
          label = 'Poll Options (A-D)';
          break;"""

switch_replacement = """        case 'poll_options':
          text = (item.poll && item.poll.options) ? item.poll.options.join('\\n') : '';
          label = 'Poll Options (A-D)';
          break;
        case 'poll_opt_0':
          text = (item.poll && item.poll.options && item.poll.options[0]) ? item.poll.options[0] : '';
          label = 'Option A';
          break;
        case 'poll_opt_1':
          text = (item.poll && item.poll.options && item.poll.options[1]) ? item.poll.options[1] : '';
          label = 'Option B';
          break;
        case 'poll_opt_2':
          text = (item.poll && item.poll.options && item.poll.options[2]) ? item.poll.options[2] : '';
          label = 'Option C';
          break;
        case 'poll_opt_3':
          text = (item.poll && item.poll.options && item.poll.options[3]) ? item.poll.options[3] : '';
          label = 'Option D';
          break;
        case 'whatsapp_post':
          text = item.whatsapp_post || '';
          label = 'WhatsApp Channel Post';
          break;"""

assert switch_target in html, "switch target not found"
html = html.replace(switch_target, switch_replacement, 1)
print("6. Updated copyCardField to support individual options and WhatsApp post.")

with open(INDEX_PATH, "w", encoding="utf-8") as f:
    f.write(html)

print("Patch applied to index.html successfully!")
