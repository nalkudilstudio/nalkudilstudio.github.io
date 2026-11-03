import os
import sys

BASE_DIR = r"D:\Websites\nalkudilstudio.github.io\nalkudil-social-studio"
INDEX_HTML = os.path.join(BASE_DIR, "index.html")

html_content = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no, viewport-fit=cover">
  <title>Nalkudil Social Studio • Autonomous Publishing Command Deck</title>
  <meta name="theme-color" content="#070B11">
  <meta name="apple-mobile-web-app-capable" content="yes">
  <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@500;600;700;800;900&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&family=Playfair+Display:ital,wght@0,600;0,700;1,600&display=swap" rel="stylesheet">
  
  <style>
    :root {
      --bg: #070B11;
      --surface: #0E1420;
      --card-bg: rgba(15, 22, 34, 0.94);
      --card-border: rgba(255, 255, 255, 0.08);
      --card-border-hover: rgba(230, 200, 117, 0.35);
      
      --gold: #E6C875;
      --gold-bright: #FFE182;
      --gold-dark: #B89230;
      
      --cyan: #00F0FF;
      --teal: #00F5D4;
      --green: #10B981;
      --magenta: #D946EF;
      --rose: #F43F5E;
      --amber: #F59E0B;
      --blue: #3B82F6;
      
      --text: #F8FAFC;
      --text-muted: #94A3B8;
      --text-dim: #64748B;
      
      --radius-sm: 8px;
      --radius-md: 14px;
      --radius-lg: 20px;
      --safe-bottom: env(safe-area-inset-bottom, 20px);
    }

    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
      -webkit-tap-highlight-color: transparent;
    }

    body {
      background-color: var(--bg);
      color: var(--text);
      font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
      min-height: 100vh;
      padding-bottom: calc(90px + var(--safe-bottom));
      background-image: 
        radial-gradient(circle at 10% 8%, rgba(0, 240, 255, 0.07), transparent 40%),
        radial-gradient(circle at 90% 12%, rgba(230, 200, 117, 0.08), transparent 45%),
        radial-gradient(circle at 50% 85%, rgba(217, 70, 239, 0.05), transparent 50%);
      background-attachment: fixed;
      overflow-x: hidden;
    }

    /* Top Sticky Brand Bar */
    .top-bar {
      position: sticky;
      top: 0;
      z-index: 100;
      backdrop-filter: blur(20px);
      -webkit-backdrop-filter: blur(20px);
      background: rgba(7, 11, 17, 0.92);
      border-bottom: 1px solid var(--card-border);
      padding: 12px 16px;
    }

    .top-bar-inner {
      max-width: 1200px;
      margin: 0 auto;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 12px;
    }

    .brand-group {
      display: flex;
      align-items: center;
      gap: 10px;
    }

    .brand-emblem {
      width: 38px;
      height: 38px;
      border-radius: 10px;
      background: linear-gradient(135deg, var(--gold-bright), var(--cyan));
      display: flex;
      align-items: center;
      justify-content: center;
      font-weight: 900;
      font-size: 19px;
      color: #070B11;
      box-shadow: 0 0 16px rgba(0, 240, 255, 0.35);
      flex-shrink: 0;
    }

    .brand-meta h1 {
      font-family: 'Outfit', sans-serif;
      font-size: 16px;
      font-weight: 800;
      letter-spacing: 0.5px;
      color: #FFF;
      display: flex;
      align-items: center;
      gap: 6px;
    }

    .brand-pill {
      font-size: 10px;
      font-weight: 700;
      text-transform: uppercase;
      padding: 2px 6px;
      border-radius: 4px;
      background: rgba(230, 200, 117, 0.15);
      color: var(--gold-bright);
      border: 1px solid rgba(230, 200, 117, 0.3);
      letter-spacing: 0.5px;
    }

    .brand-meta p {
      font-size: 11px;
      color: var(--text-muted);
      margin-top: 1px;
    }

    .top-stats {
      display: flex;
      align-items: center;
      gap: 12px;
    }

    .stat-badge {
      display: flex;
      flex-direction: column;
      align-items: flex-end;
    }

    .stat-badge .stat-num {
      font-family: 'Outfit', sans-serif;
      font-weight: 800;
      font-size: 14px;
      color: var(--teal);
    }

    .stat-badge .stat-lbl {
      font-size: 10px;
      text-transform: uppercase;
      color: var(--text-dim);
      letter-spacing: 0.5px;
    }

    /* Sticky Navigation Tabs */
    .tabs-nav-container {
      position: sticky;
      top: 63px;
      z-index: 95;
      backdrop-filter: blur(18px);
      -webkit-backdrop-filter: blur(18px);
      background: rgba(11, 16, 25, 0.95);
      border-bottom: 1px solid var(--card-border);
      padding: 8px 12px;
    }

    .tabs-nav {
      max-width: 1200px;
      margin: 0 auto;
      display: flex;
      gap: 6px;
      overflow-x: auto;
      scrollbar-width: none;
      -webkit-overflow-scrolling: touch;
      padding: 2px;
    }

    .tabs-nav::-webkit-scrollbar {
      display: none;
    }

    .nav-tab-btn {
      flex: 1;
      min-width: max-content;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 8px;
      padding: 10px 14px;
      border-radius: 10px;
      background: rgba(255, 255, 255, 0.04);
      border: 1px solid rgba(255, 255, 255, 0.08);
      color: var(--text-muted);
      font-family: 'Outfit', sans-serif;
      font-size: 13px;
      font-weight: 700;
      cursor: pointer;
      transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1);
      white-space: nowrap;
    }

    .nav-tab-btn .tab-count {
      font-size: 11px;
      padding: 2px 6px;
      border-radius: 10px;
      background: rgba(255, 255, 255, 0.08);
      color: var(--text-dim);
      font-weight: 700;
    }

    .nav-tab-btn.active {
      background: linear-gradient(135deg, rgba(230, 200, 117, 0.18), rgba(0, 240, 255, 0.12));
      border-color: var(--gold);
      color: #FFF;
      box-shadow: 0 4px 16px rgba(230, 200, 117, 0.2);
    }

    .nav-tab-btn.active .tab-count {
      background: var(--gold);
      color: #070B11;
    }

    /* Controls & Filter Bar */
    .controls-wrapper {
      max-width: 1200px;
      margin: 14px auto 8px;
      padding: 0 16px;
      display: flex;
      flex-direction: column;
      gap: 10px;
    }

    .search-row {
      display: flex;
      gap: 8px;
    }

    .search-input-box {
      flex: 1;
      position: relative;
      display: flex;
      align-items: center;
    }

    .search-input-box .search-icon {
      position: absolute;
      left: 14px;
      font-size: 14px;
      color: var(--text-dim);
      pointer-events: none;
    }

    .search-input-box input {
      width: 100%;
      background: rgba(14, 20, 32, 0.9);
      border: 1px solid var(--card-border);
      border-radius: 12px;
      padding: 12px 38px 12px 38px;
      color: #FFF;
      font-family: 'Plus Jakarta Sans', sans-serif;
      font-size: 14px;
      outline: none;
      transition: border-color 0.2s;
    }

    .search-input-box input:focus {
      border-color: var(--cyan);
      box-shadow: 0 0 12px rgba(0, 240, 255, 0.2);
    }

    .search-input-box .clear-btn {
      position: absolute;
      right: 12px;
      background: none;
      border: none;
      color: var(--text-dim);
      font-size: 16px;
      cursor: pointer;
      display: none;
      padding: 4px;
    }

    .filter-chips-row {
      display: flex;
      gap: 6px;
      overflow-x: auto;
      scrollbar-width: none;
      padding-bottom: 4px;
    }

    .filter-chips-row::-webkit-scrollbar {
      display: none;
    }

    .chip-btn {
      padding: 6px 12px;
      border-radius: 8px;
      font-size: 11.5px;
      font-weight: 600;
      background: rgba(255, 255, 255, 0.04);
      border: 1px solid rgba(255, 255, 255, 0.08);
      color: var(--text-muted);
      cursor: pointer;
      white-space: nowrap;
      transition: all 0.15s ease;
    }

    .chip-btn.active {
      background: rgba(0, 240, 255, 0.16);
      border-color: var(--cyan);
      color: var(--cyan);
      font-weight: 700;
    }

    /* Container for Cards */
    .cards-container {
      max-width: 1200px;
      margin: 12px auto;
      padding: 0 16px;
      display: flex;
      flex-direction: column;
      gap: 16px;
    }

    /* Individual Publishing Card */
    .pub-card {
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      border-radius: var(--radius-lg);
      padding: 16px;
      box-shadow: 0 8px 30px rgba(0, 0, 0, 0.45);
      transition: border-color 0.25s, transform 0.2s;
      position: relative;
    }

    .pub-card:hover {
      border-color: var(--card-border-hover);
    }

    .pub-card.is-published {
      border-color: rgba(16, 185, 129, 0.4);
      background: rgba(12, 22, 28, 0.94);
    }

    /* Card Top Bar */
    .card-top {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 10px;
      margin-bottom: 12px;
      padding-bottom: 10px;
      border-bottom: 1px solid rgba(255, 255, 255, 0.05);
      flex-wrap: wrap;
    }

    .card-meta-left {
      display: flex;
      align-items: center;
      gap: 8px;
      flex-wrap: wrap;
    }

    .ep-badge {
      font-family: 'Outfit', sans-serif;
      font-weight: 800;
      font-size: 12px;
      padding: 4px 10px;
      border-radius: 6px;
      background: linear-gradient(135deg, var(--gold), var(--gold-dark));
      color: #070B11;
      letter-spacing: 0.5px;
    }

    .ep-badge.cyan {
      background: linear-gradient(135deg, var(--cyan), #0099FF);
      color: #070B11;
    }

    .ep-badge.magenta {
      background: linear-gradient(135deg, var(--magenta), #9333EA);
      color: #FFF;
    }

    .cat-badge {
      font-size: 11px;
      font-weight: 600;
      padding: 3px 8px;
      border-radius: 6px;
      background: rgba(255, 255, 255, 0.06);
      border: 1px solid rgba(255, 255, 255, 0.1);
      color: var(--text-muted);
    }

    .slot-badge {
      font-size: 11px;
      color: var(--text-dim);
      font-weight: 500;
    }

    .status-check-label {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      cursor: pointer;
      font-size: 12px;
      font-weight: 600;
      color: var(--text-muted);
      user-select: none;
    }

    .status-check-label input {
      accent-color: var(--green);
      width: 16px;
      height: 16px;
      cursor: pointer;
    }

    .status-check-label.checked {
      color: var(--green);
    }

    /* Card Layout: Grid for Media + Content */
    .card-grid {
      display: grid;
      grid-template-columns: 180px 1fr;
      gap: 16px;
    }

    @media (max-width: 768px) {
      .card-grid {
        grid-template-columns: 1fr;
      }
    }

    /* Media Visual Box */
    .media-box {
      display: flex;
      flex-direction: column;
      gap: 8px;
    }

    .preview-thumb-wrap {
      position: relative;
      width: 100%;
      aspect-ratio: 9/16;
      border-radius: 12px;
      overflow: hidden;
      background: #04060A;
      border: 1px solid rgba(255, 255, 255, 0.1);
      display: flex;
      align-items: center;
      justify-content: center;
    }

    .preview-thumb-wrap.square {
      aspect-ratio: 1/1;
    }

    .preview-thumb-wrap.portrait-4-5 {
      aspect-ratio: 4/5;
    }

    .preview-thumb-wrap img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      display: block;
      transition: transform 0.3s;
    }

    .preview-thumb-wrap:hover img {
      transform: scale(1.04);
    }

    .thumb-placeholder {
      padding: 16px;
      text-align: center;
      font-size: 12px;
      color: var(--text-dim);
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 6px;
    }

    .btn-download-direct {
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 6px;
      width: 100%;
      padding: 8px 10px;
      border-radius: 8px;
      background: rgba(0, 240, 255, 0.12);
      border: 1px solid rgba(0, 240, 255, 0.3);
      color: var(--cyan);
      font-family: 'Outfit', sans-serif;
      font-size: 12px;
      font-weight: 700;
      text-decoration: none;
      cursor: pointer;
      transition: all 0.2s ease;
      text-align: center;
    }

    .btn-download-direct:hover {
      background: var(--cyan);
      color: #070B11;
      box-shadow: 0 4px 14px rgba(0, 240, 255, 0.35);
    }

    .dual-downloads {
      display: flex;
      flex-direction: column;
      gap: 6px;
    }

    /* Content Area */
    .content-box {
      display: flex;
      flex-direction: column;
      gap: 12px;
      min-width: 0;
    }

    .card-title-text {
      font-family: 'Outfit', sans-serif;
      font-size: 16px;
      font-weight: 700;
      line-height: 1.4;
      color: #FFF;
      word-break: break-word;
    }

    /* Quick Action Buttons Row */
    .actions-grid {
      display: flex;
      flex-wrap: wrap;
      gap: 6px;
    }

    .btn-copy {
      padding: 9px 13px;
      min-height: 38px;
      border-radius: 8px;
      font-size: 12px;
      font-weight: 700;
      font-family: 'Outfit', sans-serif;
      border: 1px solid rgba(255, 255, 255, 0.12);
      background: rgba(255, 255, 255, 0.05);
      color: var(--text);
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 6px;
      transition: all 0.18s cubic-bezier(0.16, 1, 0.3, 1);
      user-select: none;
      -webkit-user-select: none;
      touch-action: manipulation;
    }

    .btn-copy:active {
      transform: scale(0.97);
    }

    .btn-copy:hover {
      background: rgba(255, 255, 255, 0.12);
      border-color: rgba(255, 255, 255, 0.25);
      transform: translateY(-1px);
    }

    .btn-copy.gold {
      background: rgba(230, 200, 117, 0.14);
      border-color: rgba(230, 200, 117, 0.35);
      color: var(--gold-bright);
    }

    .btn-copy.gold:hover {
      background: var(--gold);
      color: #070B11;
    }

    .btn-copy.cyan {
      background: rgba(0, 240, 255, 0.14);
      border-color: rgba(0, 240, 255, 0.35);
      color: var(--cyan);
    }

    .btn-copy.cyan:hover {
      background: var(--cyan);
      color: #070B11;
    }

    .btn-copy.magenta {
      background: rgba(217, 70, 239, 0.14);
      border-color: rgba(217, 70, 239, 0.35);
      color: var(--magenta);
    }

    .btn-copy.magenta:hover {
      background: var(--magenta);
      color: #FFF;
    }

    .btn-copy.success {
      background: var(--green) !important;
      border-color: var(--green) !important;
      color: #070B11 !important;
    }

    /* Master Copy Full Packet Button */
    .btn-master-packet {
      width: 100%;
      min-height: 44px;
      padding: 11px 14px;
      border-radius: 10px;
      background: linear-gradient(135deg, rgba(230, 200, 117, 0.2), rgba(0, 240, 255, 0.15));
      border: 1px solid var(--gold);
      color: #FFF;
      font-family: 'Outfit', sans-serif;
      font-weight: 800;
      font-size: 13px;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 8px;
      transition: all 0.2s;
      user-select: none;
      -webkit-user-select: none;
      touch-action: manipulation;
    }

    .btn-master-packet:active {
      transform: scale(0.98);
    }

    /* Fallback Copy Modal (Restricted Mobile WebViews) */
    .copy-modal-backdrop {
      position: fixed;
      inset: 0;
      z-index: 1000;
      background: rgba(0, 0, 0, 0.78);
      backdrop-filter: blur(8px);
      -webkit-backdrop-filter: blur(8px);
      display: none;
      align-items: center;
      justify-content: center;
      padding: 16px;
    }
    .copy-modal-backdrop.open {
      display: flex;
    }
    .copy-modal-card {
      background: #0E1420;
      border: 1px solid rgba(230, 200, 117, 0.35);
      border-radius: 16px;
      width: 100%;
      max-width: 520px;
      max-height: 85vh;
      display: flex;
      flex-direction: column;
      padding: 18px;
      box-shadow: 0 20px 40px rgba(0,0,0,0.6);
    }
    .copy-modal-header {
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 8px;
    }
    .copy-modal-header h3 {
      font-size: 16px;
      font-weight: 700;
      color: var(--gold-bright);
      font-family: 'Outfit', sans-serif;
    }
    .btn-modal-close {
      background: transparent;
      border: none;
      color: var(--text-muted);
      font-size: 20px;
      cursor: pointer;
      padding: 4px 8px;
      line-height: 1;
    }
    .copy-modal-hint {
      font-size: 12px;
      color: var(--text-muted);
      margin-bottom: 10px;
    }
    .copy-modal-textarea {
      width: 100%;
      height: 180px;
      background: rgba(7, 11, 17, 0.95);
      border: 1px solid rgba(255, 255, 255, 0.12);
      border-radius: 10px;
      color: var(--text);
      font-family: 'JetBrains Mono', monospace;
      font-size: 12px;
      line-height: 1.5;
      padding: 10px;
      resize: vertical;
      margin-bottom: 12px;
      box-sizing: border-box;
    }
    .copy-modal-actions {
      display: flex;
      justify-content: flex-end;
      gap: 8px;
    }

    .btn-master-packet:hover {
      background: linear-gradient(135deg, var(--gold), var(--cyan));
      color: #070B11;
      box-shadow: 0 4px 18px rgba(0, 240, 255, 0.35);
    }

    .btn-master-packet.success {
      background: var(--green) !important;
      color: #070B11 !important;
      border-color: var(--green) !important;
    }

    /* Expandable / Collapsible Details */
    details.field-drawer {
      border: 1px solid rgba(255, 255, 255, 0.06);
      border-radius: 10px;
      background: #04060A;
      overflow: hidden;
    }

    details.field-drawer summary {
      padding: 8px 12px;
      font-size: 12px;
      font-weight: 600;
      color: var(--text-muted);
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: space-between;
      user-select: none;
      background: rgba(255, 255, 255, 0.02);
    }

    details.field-drawer summary:hover {
      color: #FFF;
    }

    .field-drawer-body {
      padding: 10px 12px;
      font-size: 12.5px;
      line-height: 1.6;
      color: #CBD5E1;
      white-space: pre-wrap;
      word-break: break-word;
      border-top: 1px solid rgba(255, 255, 255, 0.04);
      max-height: 220px;
      overflow-y: auto;
    }

    /* Community Poll Special Box */
    .poll-box {
      background: rgba(10, 16, 26, 0.9);
      border: 1px solid rgba(0, 240, 255, 0.2);
      border-radius: 12px;
      padding: 12px;
      display: flex;
      flex-direction: column;
      gap: 8px;
    }

    .poll-header {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 8px;
    }

    .poll-title {
      font-family: 'Outfit', sans-serif;
      font-size: 12px;
      font-weight: 800;
      color: var(--cyan);
      text-transform: uppercase;
      letter-spacing: 0.5px;
      display: flex;
      align-items: center;
      gap: 6px;
    }

    .poll-question-text {
      font-size: 13px;
      font-weight: 600;
      color: #F1F5F9;
      line-height: 1.4;
    }

    .poll-options-list {
      display: flex;
      flex-direction: column;
      gap: 4px;
      margin-top: 4px;
    }

    .poll-opt-item {
      font-size: 12px;
      padding: 4px 8px;
      border-radius: 6px;
      background: rgba(255, 255, 255, 0.04);
      color: #94A3B8;
      display: flex;
      align-items: center;
      gap: 6px;
    }

    .poll-opt-item.correct {
      border: 1px solid rgba(16, 185, 129, 0.4);
      color: #6EE7B7;
      background: rgba(16, 185, 129, 0.08);
      font-weight: 600;
    }

    .poll-actions-row {
      display: flex;
      gap: 6px;
      margin-top: 6px;
      flex-wrap: wrap;
    }

    /* Floating Toast */
    .toast-pill {
      position: fixed;
      bottom: 24px;
      left: 50%;
      transform: translateX(-50%) translateY(120px);
      background: rgba(14, 20, 32, 0.96);
      border: 1px solid var(--teal);
      color: #FFF;
      padding: 12px 24px;
      border-radius: 30px;
      font-family: 'Outfit', sans-serif;
      font-size: 13.5px;
      font-weight: 700;
      box-shadow: 0 10px 32px rgba(0, 0, 0, 0.7);
      backdrop-filter: blur(14px);
      z-index: 9999;
      opacity: 0;
      transition: all 0.28s cubic-bezier(0.16, 1, 0.3, 1);
      display: flex;
      align-items: center;
      gap: 8px;
      white-space: nowrap;
      pointer-events: none;
    }

    .toast-pill.show {
      transform: translateX(-50%) translateY(0);
      opacity: 1;
    }

    /* Floating Scroll Top */
    .btn-scroll-top {
      position: fixed;
      bottom: calc(20px + var(--safe-bottom));
      right: 18px;
      width: 44px;
      height: 44px;
      border-radius: 50%;
      background: rgba(14, 20, 32, 0.9);
      border: 1px solid var(--card-border);
      color: var(--gold-bright);
      font-size: 18px;
      font-weight: 800;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      box-shadow: 0 6px 20px rgba(0, 0, 0, 0.5);
      z-index: 80;
      opacity: 0;
      pointer-events: none;
      transition: opacity 0.2s, transform 0.2s;
    }

    .btn-scroll-top.visible {
      opacity: 1;
      pointer-events: auto;
    }

    .empty-state {
      text-align: center;
      padding: 48px 16px;
      color: var(--text-dim);
      font-size: 14px;
    }
  </style>
</head>
<body>

  <!-- Top Sticky Header -->
  <header class="top-bar">
    <div class="top-bar-inner">
      <div class="brand-group">
        <div class="brand-emblem">✦</div>
        <div class="brand-meta">
          <h1>NALKUDIL SOCIAL STUDIO <span class="brand-pill">v2026</span></h1>
          <p>Autonomous Publishing &amp; 1-Click Mobile Command Deck</p>
        </div>
      </div>
      <div class="top-stats">
        <div class="stat-badge">
          <span class="stat-num" id="stat-published-count">0 / 100</span>
          <span class="stat-lbl" id="stat-suite-label">Published</span>
        </div>
      </div>
    </div>
  </header>

  <!-- Sticky Suite Tabs -->
  <nav class="tabs-nav-container">
    <div class="tabs-nav">
      <button class="nav-tab-btn active" onclick="switchSuite('sarav_ai', this)">
        <span>🤖 Sarav × AI</span>
        <span class="tab-count" id="count-sarav">100</span>
      </button>
      <button class="nav-tab-btn" onclick="switchSuite('the_loop', this)">
        <span>🔁 The Loop</span>
        <span class="tab-count" id="count-loop">300</span>
      </button>
      <button class="nav-tab-btn" onclick="switchSuite('sid_isha', this)">
        <span>📖 Sid &amp; Isha</span>
        <span class="tab-count" id="count-sidisha">30</span>
      </button>
      <button class="nav-tab-btn" onclick="switchSuite('inkling_ig', this)">
        <span>✦ Inkling IG</span>
        <span class="tab-count" id="count-inkling">50</span>
      </button>
    </div>
  </nav>

  <!-- Search & Filter Controls -->
  <section class="controls-wrapper">
    <div class="search-row">
      <div class="search-input-box">
        <span class="search-icon">🔍</span>
        <input type="text" id="main-search-input" placeholder="Search by number (e.g. 35), day, concept, or title..." oninput="handleSearch()">
        <button class="clear-btn" id="btn-clear-search" onclick="clearSearch()">✕</button>
      </div>
    </div>

    <!-- Dynamic Category Filter Chips -->
    <div class="filter-chips-row" id="filter-chips-container">
      <!-- Injected by JavaScript -->
    </div>
  </section>

  <!-- Master Cards Render Area -->
  <main class="cards-container" id="cards-container">
    <!-- Rendered dynamically -->
  </main>

  <!-- Floating Elements -->
  <div class="toast-pill" id="toast-pill">
    <span id="toast-icon">✨</span>
    <span id="toast-msg">Copied to clipboard!</span>
  </div>

  <!-- Fallback Copy Modal for Mobile / Sandbox WebViews -->
  <div class="copy-modal-backdrop" id="copy-modal" onclick="closeCopyModal(event)">
    <div class="copy-modal-card" onclick="event.stopPropagation()">
      <div class="copy-modal-header">
        <h3 id="copy-modal-title">📋 Copy Text</h3>
        <button class="btn-modal-close" onclick="closeCopyModal(event)" aria-label="Close">✕</button>
      </div>
      <p class="copy-modal-hint">Tap inside and press Copy, or use Select All below:</p>
      <textarea class="copy-modal-textarea" id="copy-modal-textarea" readonly></textarea>
      <div class="copy-modal-actions">
        <button class="btn-copy gold" onclick="selectModalText()">Select All</button>
        <button class="btn-copy" onclick="closeCopyModal()">Done</button>
      </div>
    </div>
  </div>

  <button class="btn-scroll-top" id="btn-scroll-top" onclick="window.scrollTo({top: 0, behavior: 'smooth'})" aria-label="Back to Top">↑</button>

  <!-- Load Data -->
  <script src="catalog.js"></script>

  <script>
    // State
    let currentSuite = 'sarav_ai';
    let currentFilter = 'all';
    let currentSearchQuery = '';
    const catalog = window.PUBLISHING_CATALOG || { sarav_ai: [], the_loop: [], sid_isha: [], inkling_ig: [] };

    // Published Checklists (persisted in localStorage)
    const storageKeys = {
      sarav_ai: 'nss_published_sarav_ai',
      the_loop: 'nss_published_the_loop',
      sid_isha: 'nss_published_sid_isha',
      inkling_ig: 'nss_published_inkling_ig'
    };

    function getPublishedSet(suite) {
      try {
        const raw = localStorage.getItem(storageKeys[suite]);
        return raw ? new Set(JSON.parse(raw)) : new Set();
      } catch (e) {
        return new Set();
      }
    }

    function savePublishedSet(suite, set) {
      try {
        localStorage.setItem(storageKeys[suite], JSON.stringify(Array.from(set)));
      } catch (e) {}
    }

    function togglePublishStatus(suite, id) {
      const set = getPublishedSet(suite);
      if (set.has(id)) {
        set.delete(id);
      } else {
        set.add(id);
      }
      savePublishedSet(suite, set);
      triggerHaptic();
      updatePublishedCount();

      // Update card visual
      const cardEl = document.getElementById(`card-${suite}-${id}`);
      if (cardEl) {
        const isPub = set.has(id);
        cardEl.classList.toggle('is-published', isPub);
        const checkLabel = cardEl.querySelector('.status-check-label');
        if (checkLabel) {
          checkLabel.classList.toggle('checked', isPub);
          checkLabel.querySelector('.status-text').textContent = isPub ? 'Published ✅' : 'Pending';
        }
      }
    }

    function updatePublishedCount() {
      const items = catalog[currentSuite] || [];
      const set = getPublishedSet(currentSuite);
      const countEl = document.getElementById('stat-published-count');
      const labelEl = document.getElementById('stat-suite-label');
      if (countEl) countEl.textContent = `${set.size} / ${items.length}`;
      if (labelEl) labelEl.textContent = 'Published';
    }

    // Suite Switching
    function switchSuite(suite, btn) {
      currentSuite = suite;
      currentFilter = 'all';
      currentSearchQuery = '';
      document.getElementById('main-search-input').value = '';
      document.getElementById('btn-clear-search').style.display = 'none';

      document.querySelectorAll('.nav-tab-btn').forEach(b => b.classList.remove('active'));
      if (btn) btn.classList.add('active');

      renderFilterChips();
      renderCards();
      updatePublishedCount();
      triggerHaptic();
      window.scrollTo({ top: 0, behavior: 'smooth' });
    }

    // Search & Filter
    function handleSearch() {
      const input = document.getElementById('main-search-input');
      currentSearchQuery = input.value.trim().toLowerCase();
      document.getElementById('btn-clear-search').style.display = currentSearchQuery ? 'block' : 'none';
      renderCards();
    }

    function clearSearch() {
      document.getElementById('main-search-input').value = '';
      currentSearchQuery = '';
      document.getElementById('btn-clear-search').style.display = 'none';
      renderCards();
    }

    function setFilter(filter, chip) {
      currentFilter = filter;
      document.querySelectorAll('.chip-btn').forEach(c => c.classList.remove('active'));
      if (chip) chip.classList.add('active');
      triggerHaptic();
      renderCards();
    }

    // Filter Chips Config per Suite
    function renderFilterChips() {
      const container = document.getElementById('filter-chips-container');
      container.innerHTML = '';

      let chips = [{ id: 'all', label: 'All Items' }];

      if (currentSuite === 'sarav_ai') {
        chips.push(
          { id: 'c1', label: 'Cluster 1: LLMs (1–10)' },
          { id: 'c2', label: 'Cluster 2: Prompting (11–20)' },
          { id: 'c3', label: 'Cluster 3: RAG (21–30)' },
          { id: 'c4', label: 'Cluster 4: Agents (31–40)' },
          { id: 'upcoming', label: 'Upcoming (41–100)' },
          { id: 'pending', label: '⏳ Pending' },
          { id: 'published', label: '✅ Published' }
        );
      } else if (currentSuite === 'the_loop') {
        chips.push(
          { id: 'b1', label: 'Ep 001–050' },
          { id: 'b2', label: 'Ep 051–100' },
          { id: 'b3', label: 'Ep 101–200' },
          { id: 'b4', label: 'Ep 201–300' },
          { id: 'pending', label: '⏳ Pending' },
          { id: 'published', label: '✅ Published' }
        );
      } else if (currentSuite === 'sid_isha') {
        chips.push(
          { id: 'act1', label: 'Act I (Days 1–8)' },
          { id: 'act2', label: 'Act II (Days 9–16)' },
          { id: 'act3', label: 'Act III (Days 17–24)' },
          { id: 'act4', label: 'Act IV (Days 25–30)' },
          { id: 'pending', label: '⏳ Pending' },
          { id: 'published', label: '✅ Published' }
        );
      } else if (currentSuite === 'inkling_ig') {
        chips.push(
          { id: 'cat_memory', label: 'Memory' },
          { id: 'cat_twist', label: 'Twist' },
          { id: 'cat_love', label: 'Love' },
          { id: 'cat_scifi', label: 'Sci-Fi' },
          { id: 'cat_hope', label: 'Hope' },
          { id: 'pending', label: '⏳ Pending' },
          { id: 'published', label: '✅ Published' }
        );
      }

      chips.forEach((c, idx) => {
        const btn = document.createElement('button');
        btn.className = `chip-btn ${c.id === currentFilter ? 'active' : ''}`;
        btn.textContent = c.label;
        btn.onclick = () => setFilter(c.id, btn);
        container.appendChild(btn);
      });
    }

    // Render Cards
    function renderCards() {
      const container = document.getElementById('cards-container');
      container.innerHTML = '';

      const items = catalog[currentSuite] || [];
      const pubSet = getPublishedSet(currentSuite);

      // Filtering
      const filtered = items.filter(item => {
        // Published / Pending filter
        const isPub = pubSet.has(item.episode || item.day);
        if (currentFilter === 'pending' && isPub) return false;
        if (currentFilter === 'published' && !isPub) return false;

        // Suite specific filter
        if (currentSuite === 'sarav_ai') {
          const ep = item.episode;
          if (currentFilter === 'c1' && !(ep >= 1 && ep <= 10)) return false;
          if (currentFilter === 'c2' && !(ep >= 11 && ep <= 20)) return false;
          if (currentFilter === 'c3' && !(ep >= 21 && ep <= 30)) return false;
          if (currentFilter === 'c4' && !(ep >= 31 && ep <= 40)) return false;
          if (currentFilter === 'upcoming' && !(ep >= 41)) return false;
        } else if (currentSuite === 'the_loop') {
          const ep = item.episode;
          if (currentFilter === 'b1' && !(ep >= 1 && ep <= 50)) return false;
          if (currentFilter === 'b2' && !(ep >= 51 && ep <= 100)) return false;
          if (currentFilter === 'b3' && !(ep >= 101 && ep <= 200)) return false;
          if (currentFilter === 'b4' && !(ep >= 201 && ep <= 300)) return false;
        } else if (currentSuite === 'sid_isha') {
          const act = item.act;
          if (currentFilter === 'act1' && act !== 1) return false;
          if (currentFilter === 'act2' && act !== 2) return false;
          if (currentFilter === 'act3' && act !== 3) return false;
          if (currentFilter === 'act4' && act !== 4) return false;
        } else if (currentSuite === 'inkling_ig') {
          const cat = (item.category || '').toLowerCase();
          if (currentFilter === 'cat_memory' && !cat.includes('memory')) return false;
          if (currentFilter === 'cat_twist' && !cat.includes('twist')) return false;
          if (currentFilter === 'cat_love' && !cat.includes('love')) return false;
          if (currentFilter === 'cat_scifi' && !cat.includes('sci')) return false;
          if (currentFilter === 'cat_hope' && !cat.includes('hope')) return false;
        }

        // Text Search query
        if (currentSearchQuery) {
          const q = currentSearchQuery;
          const searchCorpus = [
            item.title,
            item.concept,
            item.description,
            item.caption,
            item.tags,
            item.hashtags,
            item.hook,
            item.twist,
            `day ${item.day}`,
            `ep ${item.episode}`,
            `${item.episode}`,
            `${item.day}`
          ].filter(Boolean).join(' ').toLowerCase();

          if (!searchCorpus.includes(q)) return false;
        }

        return true;
      });

      if (filtered.length === 0) {
        container.innerHTML = `
          <div class="empty-state">
            <p style="font-size: 28px; margin-bottom: 8px;">🔍</p>
            <p>No content matching your current filter or search.</p>
          </div>
        `;
        return;
      }

      filtered.forEach(item => {
        let cardHtml = '';
        if (currentSuite === 'sarav_ai') {
          cardHtml = buildSaravAICard(item, pubSet.has(item.episode));
        } else if (currentSuite === 'the_loop') {
          cardHtml = buildTheLoopCard(item, pubSet.has(item.episode));
        } else if (currentSuite === 'sid_isha') {
          cardHtml = buildSidIshaCard(item, pubSet.has(item.day));
        } else if (currentSuite === 'inkling_ig') {
          cardHtml = buildInklingIGCard(item, pubSet.has(item.episode));
        }
        container.insertAdjacentHTML('beforeend', cardHtml);
      });
    }

    // Builder 1: Sarav X AI
    function buildSaravAICard(item, isPublished) {
      const ep = item.episode;
      const coverUrl = item.cover_url || '';
      const poll = item.poll || {};
      const downloadName = item.cover_filename || `Sarav_AI_Shorts_Ep${String(ep).padStart(3, '0')}_Cover.png`;

      const pollOptsHtml = (poll.options || []).map((opt, i) => {
        const isCorrect = i === poll.correct_index;
        return `<div class="poll-opt-item ${isCorrect ? 'correct' : ''}">
          <b>${String.fromCharCode(65 + i)})</b> ${escapeHtml(opt)} ${isCorrect ? '✓ (Key)' : ''}
        </div>`;
      }).join('');

      return `
        <article class="pub-card ${isPublished ? 'is-published' : ''}" id="card-sarav_ai-${ep}">
          <div class="card-top">
            <div class="card-meta-left">
              <span class="ep-badge">EP #${String(ep).padStart(3, '0')}</span>
              <span class="cat-badge">${escapeHtml(item.day)}</span>
              <span class="cat-badge">${escapeHtml(item.category)}</span>
              <span class="slot-badge">🕒 18:00 IST Daily</span>
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

              <!-- Community Poll Section -->
              <div class="poll-box">
                <div class="poll-header">
                  <span class="poll-title">🗳️ YouTube Community Poll</span>
                  <button class="btn-copy cyan" style="padding: 4px 10px; font-size: 11px;" onclick="copyCardField('sarav_ai', ${ep}, 'poll_full', this)">📋 Copy Full Poll</button>
                </div>
                <p class="poll-question-text">${escapeHtml(poll.question || '')}</p>
                <div class="poll-options-list">
                  ${pollOptsHtml}
                </div>
                <div class="poll-actions-row">
                  <button class="btn-copy" style="font-size: 11px; padding: 5px 8px;" onclick="copyCardField('sarav_ai', ${ep}, 'poll_question', this)">📋 Question</button>
                  <button class="btn-copy" style="font-size: 11px; padding: 5px 8px;" onclick="copyCardField('sarav_ai', ${ep}, 'poll_options', this)">📋 Options (A-D)</button>
                </div>
              </div>

              <!-- Expandable Description & Details -->
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

    // Builder 2: The Loop
    function buildTheLoopCard(item, isPublished) {
      const ep = item.episode;
      const coverUrl = item.cover_url || '';
      const downloadName = item.cover_filename || `TheLoop_Ep${String(ep).padStart(3, '0')}_Cover.jpg`;

      return `
        <article class="pub-card ${isPublished ? 'is-published' : ''}" id="card-the_loop-${ep}">
          <div class="card-top">
            <div class="card-meta-left">
              <span class="ep-badge cyan">EP #${String(ep).padStart(3, '0')}</span>
              <span class="cat-badge">${escapeHtml(item.day)}</span>
              <span class="cat-badge">${escapeHtml(item.slot || '19:00 IST')}</span>
              <span class="cat-badge">${escapeHtml(item.category)}</span>
            </div>
            <label class="status-check-label ${isPublished ? 'checked' : ''}">
              <input type="checkbox" ${isPublished ? 'checked' : ''} onchange="togglePublishStatus('the_loop', ${ep})">
              <span class="status-text">${isPublished ? 'Published ✅' : 'Pending'}</span>
            </label>
          </div>

          <div class="card-grid">
            <div class="media-box">
              <div class="preview-thumb-wrap">
                ${coverUrl ? `<img src="${coverUrl}" alt="Ep ${ep} Cover" loading="lazy">` : `<div class="thumb-placeholder"><span>🔁</span><span>Cover Ep ${ep}</span></div>`}
              </div>
              ${coverUrl ? `<a href="${coverUrl}" download="${downloadName}" class="btn-download-direct">⬇️ Download Cover</a>` : ''}
            </div>

            <div class="content-box">
              <div style="font-size: 12px; color: var(--gold); font-style: italic;">
                "${escapeHtml(item.hook)}" / "${escapeHtml(item.twist)}"
              </div>
              <h2 class="card-title-text">${escapeHtml(item.title)}</h2>

              <div class="actions-grid">
                <button class="btn-copy gold" onclick="copyCardField('the_loop', ${ep}, 'title', this)">📋 Copy Title</button>
                <button class="btn-copy cyan" onclick="copyCardField('the_loop', ${ep}, 'description', this)">📋 Copy Description</button>
                <button class="btn-copy" onclick="copyCardField('the_loop', ${ep}, 'tags', this)">🏷️ Copy Tags</button>
                <button class="btn-copy" onclick="copyCardField('the_loop', ${ep}, 'pinned_comment', this)">📌 Pinned Comment</button>
              </div>

              <button class="btn-master-packet" onclick="copyCardField('the_loop', ${ep}, 'loop_full_packet', this)">
                ⚡ Copy Full Loop Video Packet (Title + Desc + Tags + Pinned)
              </button>

              <details class="field-drawer">
                <summary>
                  <span>View Description &amp; Loop Anchors</span>
                  <span>▾</span>
                </summary>
                <div class="field-drawer-body"><b>Description:</b><br>${escapeHtml(item.description)}<br><br><b>Tags:</b><br>${escapeHtml(item.tags)}<br><br><b>Pinned Comment:</b><br>${escapeHtml(item.pinned_comment)}</div>
              </details>
            </div>
          </div>
        </article>
      `;
    }

    // Builder 3: Sid & Isha Instagram
    function buildSidIshaCard(item, isPublished) {
      const day = item.day;
      const s1Url = item.slide1_url || '';
      const s2Url = item.slide2_url || '';

      return `
        <article class="pub-card ${isPublished ? 'is-published' : ''}" id="card-sid_isha-${day}">
          <div class="card-top">
            <div class="card-meta-left">
              <span class="ep-badge gold">DAY ${String(day).padStart(2, '0')}</span>
              <span class="cat-badge">ACT ${item.act}</span>
              <span class="cat-badge">${escapeHtml(item.date || '')}</span>
              <span class="slot-badge">🕒 10:15 AM IST Drop</span>
            </div>
            <label class="status-check-label ${isPublished ? 'checked' : ''}">
              <input type="checkbox" ${isPublished ? 'checked' : ''} onchange="togglePublishStatus('sid_isha', ${day})">
              <span class="status-text">${isPublished ? 'Published ✅' : 'Pending'}</span>
            </label>
          </div>

          <div class="card-grid">
            <div class="media-box">
              <!-- Slide 1 Thumbnail -->
              <div class="preview-thumb-wrap square">
                ${s1Url ? `<img src="${s1Url}" alt="Day ${day} Slide 1" loading="lazy">` : `<div class="thumb-placeholder">Slide 1 Art</div>`}
              </div>
              
              <!-- Direct Downloads -->
              <div class="dual-downloads">
                ${s1Url ? `<a href="${s1Url}" download="${item.slide1_filename}" class="btn-download-direct">⬇️ Slide 1 Art (1:1)</a>` : ''}
                ${s2Url ? `<a href="${s2Url}" download="${item.slide2_filename}" class="btn-download-direct" style="background: rgba(230,200,117,0.15); border-color: var(--gold); color: var(--gold-bright);">⬇️ Slide 2 Story (4:5)</a>` : ''}
              </div>
            </div>

            <div class="content-box">
              <div style="font-size: 12.5px; color: var(--gold-bright); font-style: italic;">
                Punchline: ${escapeHtml(item.punchline || '')}
              </div>
              <h2 class="card-title-text" style="font-family: 'Playfair Display', serif; font-size: 18px;">${escapeHtml(item.title)}</h2>

              <div class="actions-grid">
                <button class="btn-copy gold" onclick="copyCardField('sid_isha', ${day}, 'title', this)">📋 Copy Title</button>
                <button class="btn-copy cyan" onclick="copyCardField('sid_isha', ${day}, 'caption', this)">📖 Copy Full Caption</button>
                <button class="btn-copy" onclick="copyCardField('sid_isha', ${day}, 'hashtags', this)">🏷️ Copy Hashtags (5)</button>
                <button class="btn-copy" onclick="copyCardField('sid_isha', ${day}, 'punchline', this)">💬 Copy Punchline</button>
              </div>

              <details class="field-drawer" open>
                <summary>
                  <span>Instagram Caption Preview</span>
                  <span>▾</span>
                </summary>
                <div class="field-drawer-body">${escapeHtml(item.caption)}</div>
              </details>
            </div>
          </div>
        </article>
      `;
    }

    // Builder 4: Inkling Tales Instagram
    function buildInklingIGCard(item, isPublished) {
      const ep = item.episode;
      const coverUrl = item.cover_url || '';

      return `
        <article class="pub-card ${isPublished ? 'is-published' : ''}" id="card-inkling_ig-${ep}">
          <div class="card-top">
            <div class="card-meta-left">
              <span class="ep-badge magenta">EP #${String(ep).padStart(3, '0')}</span>
              <span class="cat-badge">${escapeHtml(item.category)}</span>
              <span class="slot-badge">🕒 19:00 IST Reel Drop</span>
            </div>
            <label class="status-check-label ${isPublished ? 'checked' : ''}">
              <input type="checkbox" ${isPublished ? 'checked' : ''} onchange="togglePublishStatus('inkling_ig', ${ep})">
              <span class="status-text">${isPublished ? 'Published ✅' : 'Pending'}</span>
            </label>
          </div>

          <div class="card-grid">
            <div class="media-box">
              <div class="preview-thumb-wrap">
                ${coverUrl ? `<img src="${coverUrl}" alt="Reel Ep ${ep} Cover" loading="lazy">` : `<div class="thumb-placeholder">Reel Ep ${ep}</div>`}
              </div>
              ${coverUrl ? `<a href="${coverUrl}" download="${item.cover_filename}" class="btn-download-direct">⬇️ Download Reel Cover</a>` : ''}
            </div>

            <div class="content-box">
              <div style="font-size: 13px; color: var(--teal); font-weight: 600;">
                "${escapeHtml(item.hook)}" / "${escapeHtml(item.twist)}"
              </div>
              <h2 class="card-title-text">Inkling Tales • Ep. ${String(ep).padStart(3, '0')} (${escapeHtml(item.category)})</h2>

              <div class="actions-grid">
                <button class="btn-copy gold" onclick="copyCardField('inkling_ig', ${ep}, 'title', this)">📋 Copy Title</button>
                <button class="btn-copy cyan" onclick="copyCardField('inkling_ig', ${ep}, 'caption', this)">📖 Copy Reel Caption</button>
                <button class="btn-copy" onclick="copyCardField('inkling_ig', ${ep}, 'hashtags', this)">🏷️ Copy Hashtags</button>
                ${item.alt_text ? `<button class="btn-copy" onclick="copyCardField('inkling_ig', ${ep}, 'alt_text', this)">♿ Copy Alt Text</button>` : ''}
              </div>

              <details class="field-drawer" open>
                <summary>
                  <span>Reel Caption Preview</span>
                  <span>▾</span>
                </summary>
                <div class="field-drawer-body">${escapeHtml(item.caption)}</div>
              </details>
            </div>
          </div>
        </article>
      `;
    }

    // Universal Master Field Copy Helper
    function copyCardField(suite, id, field, btnElement) {
      const items = catalog[suite] || [];
      const item = items.find(x => (suite === 'sid_isha' ? x.day === id : x.episode === id));
      if (!item) {
        showToast('⚠️ Item not found in catalog.');
        return;
      }

      let text = '';
      let label = 'Text';

      switch (field) {
        case 'title':
          text = item.title || (suite === 'inkling_ig' ? `Inkling Tales • Ep. ${String(id).padStart(3, '0')} (${item.category || ''})` : '');
          label = 'Title';
          break;
        case 'description':
          text = item.description || '';
          label = 'Description';
          break;
        case 'tags':
          text = item.tags || '';
          label = 'Tags';
          break;
        case 'pinned_comment':
          text = item.pinned_comment || '';
          label = 'Pinned Comment';
          break;
        case 'sarav_full_packet':
          text = `TITLE:\\n${item.title || ''}\\n\\nDESCRIPTION:\\n${item.description || ''}\\n\\nTAGS:\\n${item.tags || ''}\\n\\nPINNED COMMENT:\\n${item.pinned_comment || ''}`;
          label = 'Full Shorts Packet';
          break;
        case 'loop_full_packet':
          text = `TITLE:\\n${item.title || ''}\\n\\nDESCRIPTION:\\n${item.description || ''}\\n\\nTAGS:\\n${item.tags || ''}\\n\\nPINNED COMMENT:\\n${item.pinned_comment || ''}`;
          label = 'Full Loop Video Packet';
          break;
        case 'poll_full':
          text = (item.poll && item.poll.full_text) ? item.poll.full_text : '';
          label = 'Full Poll';
          break;
        case 'poll_question':
          text = (item.poll && item.poll.question) ? item.poll.question : '';
          label = 'Poll Question';
          break;
        case 'poll_options':
          text = (item.poll && item.poll.options) ? item.poll.options.join('\\n') : '';
          label = 'Poll Options (A-D)';
          break;
        case 'caption':
          text = item.caption || '';
          label = (suite === 'sid_isha') ? 'Full Caption' : 'Reel Caption';
          break;
        case 'hashtags':
          text = item.hashtags || '';
          label = 'Hashtags';
          break;
        case 'punchline':
          text = item.punchline || '';
          label = 'Punchline';
          break;
        case 'alt_text':
          text = item.alt_text || '';
          label = 'Alt Text';
          break;
        default:
          text = item[field] || '';
          label = field;
      }

      copySnippet(text, btnElement, label);
    }

    // Packet Copy Helpers (Wrappers for backward compatibility)
    function copySaravFullPacket(ep, btn) {
      copyCardField('sarav_ai', ep, 'sarav_full_packet', btn);
    }

    function copyLoopFullPacket(ep, btn) {
      copyCardField('the_loop', ep, 'loop_full_packet', btn);
    }

    // Multi-Tier Mobile & Desktop Clipboard Engine
    async function copySnippet(text, btnElement, label = 'Text') {
      if (!text) {
        showToast(`⚠️ No ${label} available to copy.`);
        return;
      }

      let copied = false;

      // Tier 1: Modern Async Clipboard API (Secure Context on Mobile & Desktop)
      if (navigator.clipboard && window.isSecureContext) {
        try {
          await navigator.clipboard.writeText(text);
          copied = true;
        } catch (err) {
          copied = false;
        }
      }

      // Tier 2: Synchronous execCommand Fallback (iOS Safari, Android WebViews)
      if (!copied) {
        copied = fallbackCopyExec(text);
      }

      // Outcome Handling
      if (copied) {
        showCopySuccess(btnElement, label);
      } else {
        // Tier 3: Manual Modal for strictly sandboxed WebViews
        showFallbackModal(text, label);
      }
    }

    function fallbackCopyExec(text) {
      let success = false;
      const ta = document.createElement('textarea');
      ta.value = text;

      // Mobile WebKit optimization (prevent zoom, layout shift, keyboard popup)
      ta.style.fontSize = '16px';
      ta.style.position = 'fixed';
      ta.style.top = '0';
      ta.style.left = '-9999px';
      ta.style.width = '2em';
      ta.style.height = '2em';
      ta.style.padding = '0';
      ta.style.border = 'none';
      ta.style.outline = 'none';
      ta.style.boxShadow = 'none';
      ta.style.background = 'transparent';
      ta.setAttribute('readonly', '');

      document.body.appendChild(ta);

      try {
        if (/iPad|iPhone|iPod/.test(navigator.userAgent) && !window.MSStream) {
          const range = document.createRange();
          range.selectNodeContents(ta);
          const sel = window.getSelection();
          if (sel) {
            sel.removeAllRanges();
            sel.addRange(range);
          }
          ta.setSelectionRange(0, 999999);
        } else {
          ta.select();
          ta.setSelectionRange(0, ta.value.length);
        }

        success = document.execCommand('copy');
      } catch (err) {
        success = false;
      } finally {
        document.body.removeChild(ta);
      }

      return success;
    }

    function showCopySuccess(btnElement, label) {
      triggerHaptic();
      showToast(`✨ Copied ${label} to clipboard!`);

      if (btnElement) {
        const originalHtml = btnElement.getAttribute('data-original-html') || btnElement.innerHTML;
        if (!btnElement.getAttribute('data-original-html')) {
          btnElement.setAttribute('data-original-html', originalHtml);
        }
        btnElement.classList.add('success');
        btnElement.innerHTML = `✅ Copied!`;
        clearTimeout(btnElement._copyResetTimer);
        btnElement._copyResetTimer = setTimeout(() => {
          btnElement.classList.remove('success');
          btnElement.innerHTML = btnElement.getAttribute('data-original-html') || originalHtml;
        }, 1600);
      }
    }

    // Modal Copy Dialog Fallback
    function showFallbackModal(text, label) {
      const modal = document.getElementById('copy-modal');
      const title = document.getElementById('copy-modal-title');
      const textarea = document.getElementById('copy-modal-textarea');
      if (!modal || !textarea) return;

      if (title) title.textContent = `📋 Copy ${label}`;
      textarea.value = text;
      modal.classList.add('open');
      textarea.focus();
      textarea.select();
    }

    function closeCopyModal(event) {
      if (event && event.target && event.target.id !== 'copy-modal' && !event.target.classList.contains('btn-modal-close')) {
        return;
      }
      const modal = document.getElementById('copy-modal');
      if (modal) modal.classList.remove('open');
    }

    function selectModalText() {
      const textarea = document.getElementById('copy-modal-textarea');
      if (textarea) {
        textarea.focus();
        textarea.select();
        textarea.setSelectionRange(0, textarea.value.length);
        showToast('✨ Text selected! Tap Copy in your menu.');
      }
    }

    function triggerHaptic() {
      if (navigator.vibrate) {
        navigator.vibrate(40);
      }
    }

    let toastTimer = null;
    function showToast(msg) {
      const toast = document.getElementById('toast-pill');
      const msgEl = document.getElementById('toast-msg');
      if (!toast || !msgEl) return;

      msgEl.textContent = msg;
      toast.classList.add('show');

      clearTimeout(toastTimer);
      toastTimer = setTimeout(() => {
        toast.classList.remove('show');
      }, 2400);
    }

    function escapeHtml(str) {
      if (!str) return '';
      return String(str)
        .replace(/&/g, '&amp;')
        .replace(/</g, '&lt;')
        .replace(/>/g, '&gt;')
        .replace(/"/g, '&quot;')
        .replace(/'/g, '&#039;');
    }

    // Scroll Top Button visibility
    window.addEventListener('scroll', () => {
      const btn = document.getElementById('btn-scroll-top');
      if (btn) {
        btn.classList.toggle('visible', window.scrollY > 300);
      }
    });

    // Initialize
    window.addEventListener('DOMContentLoaded', () => {
      renderFilterChips();
      renderCards();
      updatePublishedCount();
    });
  </script>
</body>
</html>
"""

with open(INDEX_HTML, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"Master index.html written successfully! (Size: {len(html_content)/1024:.1f} KB)")
