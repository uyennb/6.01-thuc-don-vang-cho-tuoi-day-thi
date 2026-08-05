import os

html_content = """<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>BÀI H6.01: THỰC ĐƠN VÀNG CHO TUỔI DẬY THÌ - NOVA HOSPITAL (22 SLIDES)</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@600;700;800&family=Montserrat:wght@700;800;900&display=swap" rel="stylesheet">
  <style>
    /* DESIGN SYSTEM: DIGITAL HEALTH (Y TẾ KỸ THUẬT SỐ) - PERFECTLY CENTERED & 8 DOCTOR CONCEPT STAGES (22 SLIDES) */
    * { box-sizing: border-box; margin: 0; padding: 0; user-select: none; }
    body {
      font-family: 'Inter', sans-serif;
      background: #F9FAFB url('hinh-nen-powerpoint-y-te-38.jpg') no-repeat center center fixed;
      background-size: cover;
      color: #1E293B;
      min-height: 100vh;
      overflow: hidden;
      display: flex;
      flex-direction: column;
    }

    .bg-overlay {
      position: fixed; top: 0; left: 0; right: 0; bottom: 0;
      background: rgba(249, 250, 251, 0.85);
      backdrop-filter: blur(4px);
      z-index: 0;
    }

    #app {
      position: relative;
      z-index: 10;
      display: flex;
      flex-direction: column;
      height: 100vh;
      width: 100vw;
    }

    header {
      height: 75px;
      padding: 0 35px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      border-bottom: 2.5px solid #0F766E;
      background: rgba(230, 247, 245, 0.96);
      backdrop-filter: blur(12px);
      box-shadow: 0 4px 15px rgba(12, 78, 75, 0.1);
    }
    .header-left, .header-right { display: flex; align-items: center; gap: 18px; }
    .btn-header {
      background: #FFFFFF;
      border: 2px solid #0F766E;
      color: #0F766E;
      padding: 10px 22px;
      border-radius: 22px;
      font-weight: 700;
      font-size: 15px;
      cursor: pointer;
      transition: all 0.2s ease;
      display: flex; align-items: center; gap: 8px;
      box-shadow: 0 2px 6px rgba(15, 118, 110, 0.12);
    }
    .btn-header:hover {
      background: #0F766E;
      color: #FFFFFF;
      box-shadow: 0 4px 14px rgba(15, 118, 110, 0.3);
      transform: translateY(-1px);
    }
    .brand-badge {
      display: flex; align-items: center; gap: 12px;
      background: #FFFFFF;
      border: 2px solid #0F766E;
      padding: 8px 22px; border-radius: 30px;
      box-shadow: 0 2px 10px rgba(15, 118, 110, 0.15);
    }
    .brand-badge .icon { font-size: 22px; }
    .brand-badge .text {
      font-family: 'Montserrat', sans-serif;
      font-weight: 800; font-size: 16px;
      color: #0C4E4B;
      letter-spacing: 0.5px;
    }
    .stage-badge {
      background: #E6F7F5;
      border: 2px solid #0F766E;
      color: #0C4E4B;
      padding: 8px 20px; border-radius: 22px;
      font-size: 15px; font-weight: 800;
    }

    main {
      flex: 1;
      position: relative;
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 20px;
    }

    .slide {
      position: absolute;
      width: 100%;
      max-width: 1280px;
      max-height: calc(100vh - 170px);
      opacity: 0;
      visibility: hidden;
      transition: all 0.4s ease-in-out;
      transform: scale(0.97);
      display: flex;
      flex-direction: column;
      background: rgba(255, 255, 255, 0.96);
      border: 2px solid #0F766E;
      border-radius: 28px;
      padding: 35px 45px;
      box-shadow: 0 12px 40px rgba(12, 78, 75, 0.15);
      overflow-y: auto;
      margin: auto 0;
    }

    .slide.active {
      opacity: 1;
      visibility: visible;
      transform: scale(1);
    }

    .slide-title {
      font-family: 'Montserrat', sans-serif;
      font-size: 28px;
      font-weight: 900;
      color: #0C4E4B;
      margin-bottom: 25px;
      display: flex;
      align-items: center;
      gap: 15px;
      border-bottom: 2px solid #E6F7F5;
      padding-bottom: 12px;
      text-wrap: balance;
    }
    .slide-title .tag {
      background: #0F766E;
      color: #FFFFFF;
      font-size: 14px;
      padding: 6px 14px;
      border-radius: 12px;
      font-weight: 800;
      letter-spacing: 0.5px;
      white-space: nowrap;
    }

    .slide-body {
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 22px;
      flex: 1;
    }

    .grid-2 { display: grid; grid-template-columns: 1fr 1fr; gap: 24px; width: 100%; }
    .grid-3 { display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 20px; width: 100%; }

    .card {
      background: #FFFFFF;
      border: 2px solid #0F766E;
      border-radius: 20px;
      padding: 24px;
      box-shadow: 0 4px 12px rgba(15, 118, 110, 0.08);
      transition: all 0.25s ease;
      display: flex;
      flex-direction: column;
      gap: 12px;
    }
    .card:hover {
      transform: translateY(-3px);
      box-shadow: 0 8px 22px rgba(15, 118, 110, 0.18);
    }
    .card-title {
      font-family: 'Montserrat', sans-serif;
      font-size: 20px;
      font-weight: 800;
      color: #0C4E4B;
    }
    .card-desc {
      font-size: 16px;
      color: #475569;
      line-height: 1.6;
    }

    /* Stage Banner Slide Style */
    .banner-card {
      background: linear-gradient(135deg, #E6F7F5, #FFFFFF);
      border: 3px solid #0F766E;
      border-radius: 30px;
      padding: 40px;
      width: 100%;
      max-width: 950px;
      text-align: center;
      box-shadow: 0 10px 30px rgba(15, 118, 110, 0.15);
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 20px;
    }
    .banner-stage-tag {
      background: linear-gradient(135deg, #0C4E4B, #0F766E);
      color: #FFFFFF;
      font-size: 20px;
      font-weight: 800;
      padding: 10px 30px;
      border-radius: 25px;
      letter-spacing: 0.5px;
      box-shadow: 0 4px 12px rgba(12, 78, 75, 0.2);
    }

    /* Mini Game 1 Keyword Styles */
    .dossier-box {
      background: #FFFFFF;
      border: 2px solid #0F766E;
      border-radius: 18px;
      padding: 20px;
      width: 100%;
      text-align: left;
    }
    .dossier-title {
      font-family: 'Montserrat', sans-serif;
      font-size: 18px;
      font-weight: 800;
      color: #0C4E4B;
      margin-bottom: 10px;
      display: flex;
      align-items: center;
      gap: 8px;
    }
    .dossier-content {
      font-size: 17px;
      line-height: 1.8;
      color: #1E293B;
    }
    .habit-kw {
      cursor: pointer;
      padding: 2px 6px;
      border-radius: 6px;
      transition: all 0.2s ease;
      display: inline-block;
    }
    .habit-kw:hover {
      background: #E6F7F5;
    }
    .habit-kw.found {
      text-decoration: underline;
      border-bottom: 3.5px solid #DC2626;
      background: #FEE2E2;
      color: #991B1B;
      font-weight: 700;
      animation: doubleBlink 0.9s ease-in-out;
    }

    @keyframes doubleBlink {
      0%, 100% { opacity: 1; transform: scale(1); }
      25%, 75% { opacity: 0.3; transform: scale(1.06); }
      50% { opacity: 1; transform: scale(1.03); }
    }

    /* SVG Connecting Game 2 */
    .matrix-container {
      display: flex;
      justify-content: space-between;
      align-items: stretch;
      gap: 50px;
      position: relative;
      width: 100%;
      padding: 10px 0;
    }
    .matrix-col {
      display: flex;
      flex-direction: column;
      gap: 15px;
      flex: 1;
      z-index: 2;
    }
    .matrix-item {
      background: #FFFFFF;
      border: 2.5px solid #0F766E;
      border-radius: 16px;
      padding: 16px 20px;
      font-size: 16px;
      font-weight: 700;
      color: #0C4E4B;
      cursor: pointer;
      transition: all 0.2s ease;
      display: flex;
      align-items: center;
      justify-content: space-between;
      min-height: 60px;
    }
    .matrix-item:hover {
      background: #E6F7F5;
      transform: scale(1.02);
    }
    .matrix-item.selected {
      background: #0F766E;
      color: #FFFFFF;
      border-color: #0C4E4B;
      box-shadow: 0 4px 14px rgba(15, 118, 110, 0.3);
    }
    .matrix-item.matched {
      background: #D1FAE5;
      border-color: #059669;
      color: #065F46;
      cursor: default;
    }
    #matrixSvg {
      position: absolute;
      top: 0; left: 0;
      width: 100%; height: 100%;
      pointer-events: none;
      z-index: 1;
    }

    /* Game 3 Nutrient Station Drag & Drop Progressive Styles */
    .station-container {
      display: flex;
      flex-direction: column;
      gap: 16px;
      width: 55%;
    }
    .station-card {
      background: #FFFFFF;
      border: 2.5px solid #0F766E;
      border-radius: 20px;
      padding: 18px 22px;
      display: flex;
      flex-direction: column;
      gap: 10px;
      transition: all 0.3s ease;
    }
    .station-card.drag-over {
      background: #E6F7F5;
      border-color: #059669;
      transform: scale(1.02);
    }
    .station-card.filled {
      border-color: #059669;
      background: #F0FDF4;
    }
    .station-title {
      font-family: 'Montserrat', sans-serif;
      font-size: 17px;
      font-weight: 800;
      color: #0C4E4B;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }
    .station-progress-bg {
      height: 14px;
      background: #E2E8F0;
      border-radius: 10px;
      overflow: hidden;
    }
    .station-progress-bar {
      height: 100%;
      width: 0%;
      background: linear-gradient(90deg, #0F766E, #059669);
      transition: width 0.4s ease;
    }
    .food-tag-container {
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
      min-height: 38px;
    }
    .food-tag-station {
      background: #E6F7F5;
      color: #0C4E4B;
      font-size: 14px;
      font-weight: 700;
      padding: 5px 12px;
      border-radius: 12px;
      border: 1px solid #0F766E;
    }

    .food-pantry {
      display: flex;
      flex-wrap: wrap;
      gap: 12px;
      background: #FFFFFF;
      border: 2.5px solid #0F766E;
      border-radius: 20px;
      padding: 20px;
      min-height: 250px;
    }
    .food-chip {
      background: #FFFFFF;
      border: 2px solid #0F766E;
      color: #0C4E4B;
      padding: 10px 16px;
      border-radius: 16px;
      font-size: 15px;
      font-weight: 700;
      cursor: grab;
      transition: all 0.2s ease;
      box-shadow: 0 2px 6px rgba(15, 118, 110, 0.1);
    }
    .food-chip:hover {
      background: #E6F7F5;
      transform: translateY(-2px);
    }
    .food-chip.disabled {
      opacity: 0.35;
      pointer-events: none;
      cursor: not-allowed;
    }

    /* Instant Feedback Animations */
    .flash-green-anim {
      animation: flashGreen 0.6s ease-in-out;
    }
    .flash-red-anim {
      animation: flashRed 0.6s ease-in-out;
    }
    .card-snapback-anim {
      animation: cardSnapback 0.5s ease-in-out;
    }

    @keyframes flashGreen {
      0%, 100% { background: #FFFFFF; }
      50% { background: #D1FAE5; border-color: #059669; }
    }
    @keyframes flashRed {
      0%, 100% { background: #FFFFFF; }
      50% { background: #FEE2E2; border-color: #DC2626; }
    }
    @keyframes cardSnapback {
      0% { transform: scale(1); }
      30% { transform: translateX(-12px) scale(1.05); }
      60% { transform: translateX(12px) scale(0.95); }
      100% { transform: translateX(0) scale(1); }
    }

    /* Timer Styles */
    .timer-box {
      font-family: 'JetBrains Mono', monospace;
      font-size: 22px;
      font-weight: 800;
      color: #DC2626;
      background: #FEE2E2;
      border: 2px solid #DC2626;
      padding: 6px 16px;
      border-radius: 14px;
      display: inline-flex;
      align-items: center;
      gap: 10px;
    }
    .btn-timer-start {
      background: #DC2626;
      color: #FFFFFF;
      border: none;
      padding: 6px 14px;
      border-radius: 10px;
      font-size: 13px;
      font-weight: 800;
      cursor: pointer;
    }

    /* Modal Glassmorphism UI */
    .modal-overlay {
      position: fixed; top: 0; left: 0; right: 0; bottom: 0;
      background: rgba(15, 23, 42, 0.65);
      backdrop-filter: blur(8px);
      z-index: 100;
      display: none;
      align-items: center;
      justify-content: center;
    }
    .modal-overlay.open { display: flex; }
    .modal-card {
      background: #FFFFFF;
      border: 3px solid #0F766E;
      border-radius: 28px;
      padding: 35px 45px;
      max-width: 550px;
      width: 90%;
      text-align: center;
      box-shadow: 0 20px 50px rgba(12, 78, 75, 0.3);
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 18px;
    }

    /* Footer Nav */
    footer {
      height: 70px;
      padding: 0 35px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      background: rgba(230, 247, 245, 0.96);
      backdrop-filter: blur(12px);
      border-top: 2px solid #0F766E;
    }
    .btn-nav {
      background: #0F766E;
      color: #FFFFFF;
      border: none;
      padding: 12px 28px;
      border-radius: 22px;
      font-weight: 800;
      font-size: 16px;
      cursor: pointer;
      transition: all 0.2s ease;
      box-shadow: 0 4px 12px rgba(15, 118, 110, 0.25);
    }
    .btn-nav:hover:not(:disabled) {
      background: #0C4E4B;
      transform: translateY(-2px);
    }
    .btn-nav:disabled {
      opacity: 0.4; cursor: not-allowed;
    }
    .slide-counter {
      font-family: 'Montserrat', sans-serif;
      font-weight: 800;
      font-size: 18px;
      color: #0C4E4B;
    }

    /* Drawer Sidebar */
    .drawer-overlay {
      position: fixed; top: 0; left: 0; right: 0; bottom: 0;
      background: rgba(15, 23, 42, 0.5);
      z-index: 90; display: none;
    }
    .drawer-overlay.open { display: block; }
    .drawer {
      position: fixed; top: 0; right: -380px; width: 380px; height: 100vh;
      background: #FFFFFF;
      border-left: 3px solid #0F766E;
      z-index: 95;
      transition: right 0.3s ease;
      display: flex; flex-direction: column;
      box-shadow: -10px 0 30px rgba(12, 78, 75, 0.2);
    }
    .drawer.open { right: 0; }
    .drawer-header {
      padding: 20px 25px;
      border-bottom: 2px solid #E6F7F5;
      display: flex; justify-content: space-between; align-items: center;
      background: #E6F7F5;
    }
    .drawer-title {
      font-family: 'Montserrat', sans-serif;
      font-size: 20px; font-weight: 800; color: #0C4E4B;
    }
    .drawer-list {
      flex: 1; overflow-y: auto; padding: 15px;
      display: flex; flex-direction: column; gap: 10px;
    }
    .drawer-item {
      padding: 14px 18px; border-radius: 14px;
      border: 1.5px solid #E2E8F0;
      font-size: 15px; font-weight: 700; color: #334155;
      cursor: pointer; transition: all 0.2s ease;
      text-align: left;
    }
    .drawer-item:hover, .drawer-item.active {
      background: #E6F7F5; border-color: #0F766E; color: #0C4E4B;
    }

    .btn-action {
      background: linear-gradient(135deg, #0F766E, #0C4E4B);
      color: #FFFFFF; border: none;
      padding: 15px 38px; border-radius: 26px;
      font-weight: 800; font-size: 18px;
      cursor: pointer; transition: all 0.25s ease;
      box-shadow: 0 6px 20px rgba(15, 118, 110, 0.3);
      margin-top: 10px;
    }
    .btn-action:hover {
      transform: translateY(-2px);
      box-shadow: 0 8px 25px rgba(15, 118, 110, 0.4);
    }

    .mindmap-node {
      background: #FFFFFF; border: 2.5px solid #0F766E;
      border-radius: 20px; padding: 22px; text-align: left;
    }
    .mindmap-header {
      font-family: 'Montserrat', sans-serif; font-size: 20px; font-weight: 800;
      color: #0C4E4B; margin-bottom: 10px; border-bottom: 2px solid #E6F7F5; padding-bottom: 6px;
    }

    .habit-item {
      display: flex; align-items: center; gap: 14px;
      background: #FFFFFF; border: 2px solid #0F766E;
      padding: 14px 20px; border-radius: 16px; font-size: 17px; font-weight: 700;
      color: #0C4E4B; cursor: pointer; transition: all 0.2s ease;
    }
    .habit-item:hover { background: #E6F7F5; }
    .habit-item.checked { background: #D1FAE5; border-color: #059669; color: #065F46; }
    .checkbox-icon {
      width: 24px; height: 24px; border: 2px solid #0F766E; border-radius: 6px;
      display: flex; align-items: center; justify-content: center; font-size: 14px; font-weight: 900;
    }
    .habit-item.checked .checkbox-icon { background: #059669; border-color: #059669; color: #FFFFFF; }

    .cert-card {
      background: linear-gradient(135deg, #FFFFFF, #E6F7F5);
      border: 4px solid #0F766E; border-radius: 30px;
      padding: 35px; text-align: center; width: 100%; max-width: 800px;
      box-shadow: 0 15px 40px rgba(12, 78, 75, 0.2);
    }
    .cert-title {
      font-family: 'Montserrat', sans-serif; font-size: 32px; font-weight: 900; color: #0C4E4B;
    }

    #confettiCanvas { position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; pointer-events: none; z-index: 99; }
  </style>
</head>
<body>
<div class="bg-overlay"></div>
<canvas id="confettiCanvas"></canvas>

<div id="app">
  <!-- Header -->
  <header>
    <div class="header-left">
      <div class="brand-badge">
        <span class="icon">🩺</span>
        <span class="text">NOVA HOSPITAL - KHOA DINH DƯỠNG</span>
      </div>
      <div class="stage-badge" id="stageBadge">Khoa Dinh dưỡng - Nova Hospital</div>
    </div>
    <div class="header-right">
      <button class="btn-header" onclick="goToSlide(0)">🏠 Trang chủ</button>
      <button class="btn-header" onclick="toggleDrawer()">☰ Danh sách slide (22)</button>
    </div>
  </header>

  <!-- Slide Viewport -->
  <main>
    <!-- SLIDE 1 [MĐ01]: MỞ ĐẦU BÀI HỌC -->
    <section class="slide active" id="slide-0">
      <div class="slide-body" style="justify-content: center; text-align: center;">
        <div style="background: #E6F7F5; border: 2px solid #0F766E; padding: 10px 28px; border-radius: 20px; font-weight: 800; font-size: 16px; color: #0F766E; display: inline-block;">
          CHƯƠNG TRÌNH KỸ NĂNG SỐNG NOVASTARS - KHỐI 6
        </div>
        <h1 style="font-family: 'Montserrat', sans-serif; font-size: 48px; font-weight: 900; color: #0C4E4B; margin-top: 15px; margin-bottom: 10px;">
          THỰC ĐƠN VÀNG CHO TUỔI DẬY THÌ
        </h1>
        <p style="font-size: 22px; max-width: 900px; color: #475569; line-height: 1.6;">
          Bảo vệ vóc dáng, bứt phá chiều cao, phát triển trí não và cân bằng thể chất cùng Kíp trực Bác sĩ Dinh dưỡng Nova Hospital.
        </p>
        <button class="btn-action" style="font-size: 20px; padding: 18px 45px;" onclick="nextSlide()">
          [ 🩺 BẮT ĐẦU PHIÊN KHÁM Y KHOA ➔ ]
        </button>
      </div>
    </section>

    <!-- SLIDE 2 [MT01]: MỤC TIÊU BÀI HỌC (GĐ1) -->
    <section class="slide" id="slide-1">
      <h2 class="slide-title"><span class="tag">MỤC TIÊU</span> MỤC TIÊU BÀI HỌC (KIẾN THỨC - KỸ NĂNG - THÁI ĐỘ)</h2>
      <div class="slide-body">
        <div class="grid-3" style="align-items: stretch;">
          <div class="card" style="border-top: 5px solid #0F766E; min-height: 260px;">
            <div class="card-title" style="color: #0F766E; font-size: 22px; border-bottom: 2px solid #E6F7F5; padding-bottom: 8px;">🧠 1. KIẾN THỨC (K)</div>
            <div class="card-desc" style="font-size: 17px; text-align: left; line-height: 1.7; color: #334155;">
              • Nhận biết được các nhóm chất dinh dưỡng cần thiết cho cơ thể trong giai đoạn tuổi dậy thì.<br><br>
              • Hiểu rõ nhu cầu năng lượng và sự phát triển thể chất đặc thù của lứa tuổi THCS.
            </div>
          </div>
          <div class="card" style="border-top: 5px solid #D97706; min-height: 260px;">
            <div class="card-title" style="color: #D97706; font-size: 22px; border-bottom: 2px solid #FEF3C7; padding-bottom: 8px;">🛠️ 2. KỸ NĂNG (S)</div>
            <div class="card-desc" style="font-size: 17px; text-align: left; line-height: 1.7; color: #334155;">
              • Áp dụng kiến thức dinh dưỡng để tự thiết kế một thực đơn vàng cân bằng, hợp lý cho bản thân trong 1 ngày.
            </div>
          </div>
          <div class="card" style="border-top: 5px solid #059669; min-height: 260px;">
            <div class="card-title" style="color: #059669; font-size: 22px; border-bottom: 2px solid #D1FAE5; padding-bottom: 8px;">❤️ 3. THÁI ĐỘ (A)</div>
            <div class="card-desc" style="font-size: 17px; text-align: left; line-height: 1.7; color: #334155;">
              • Có ý thức chủ động chăm sóc sức khỏe thể chất.<br><br>
              • Tự giác lựa chọn thực phẩm lành mạnh và hạn chế đồ ăn nhanh.
            </div>
          </div>
        </div>
        <div style="background: #E6F7F5; border: 2px solid #0F766E; padding: 16px 30px; border-radius: 18px; text-align: center; width: 100%;">
          <p style="font-size: 19px; font-weight: 800; color: #0C4E4B; margin: 0;">🎯 Sẵn sàng chinh phục mục tiêu cùng Kíp trực Bác sĩ Dinh dưỡng Nova Hospital!</p>
        </div>
        <div style="text-align: center;">
          <button class="btn-action" style="font-size: 19px; padding: 16px 42px;" onclick="nextSlide()">[ BẮT ĐẦU NHIỆM VỤ Y KHOA ➔ ]</button>
        </div>
      </div>
    </section>

    <!-- SLIDE 3 [GT01]: NHIỆM VỤ BÀI HỌC (GĐ1) -->
    <section class="slide" id="slide-2">
      <h2 class="slide-title"><span class="tag">BÀI HỌC</span> NHIỆM VỤ CỦA KÍP TRỰC BÁC SĨ DINH DƯỠNG</h2>
      <div class="slide-body">
        <div class="grid-3">
          <div class="card">
            <div class="card-title">🚨 Nhiệm vụ 1</div>
            <div class="card-desc">Tiếp nhận và giải mã 3 hồ sơ ca bệnh bất ổn thể chất (mệt mỏi, nổi mụn, sút cân, béo phì) của học sinh 12 tuổi.</div>
          </div>
          <div class="card">
            <div class="card-title">🔍 Nhiệm vụ 2</div>
            <div class="card-desc">Hội chẩn giải mã ma trận dinh dưỡng cho 5 hệ cơ quan (Thần kinh, Cơ xương, Nội tiết, Cảm xúc, Da).</div>
          </div>
          <div class="card">
            <div class="card-title">🍱 Nhiệm vụ 3</div>
            <div class="card-desc">Kê đơn Thực đơn vàng 1 ngày cân đối 4 nhóm chất và cam kết thói quen ăn uống chuẩn y khoa.</div>
          </div>
        </div>
        <div style="background: #E6F7F5; border: 2px solid #0F766E; padding: 24px 30px; border-radius: 20px; text-align: center; width: 100%;">
          <p style="font-size: 22px; font-weight: 800; color: #0C4E4B;">👨‍⚕️ Các bác sĩ tập sự hãy sẵn sàng đeo thẻ kíp trực và chuyển sang Giai đoạn 2!</p>
        </div>
      </div>
    </section>

    <!-- SLIDE 4 [STAGE BANNER GĐ2]: NHẬN HỒ SƠ BỆNH ÁN -->
    <section class="slide" id="slide-3">
      <div class="slide-body" style="justify-content: center; align-items: center; text-align: center;">
        <div class="banner-card">
          <div class="banner-stage-tag">🩺 CONCEPT BÁC SĨ NOVA HOSPITAL - GIAI ĐOẠN 2</div>
          <div style="font-size: 70px;">📋</div>
          <h2 style="font-family: 'Montserrat', sans-serif; font-size: 38px; font-weight: 900; color: #0C4E4B;">
            GIAI ĐOẠN 2: NHẬN HỒ SƠ BỆNH ÁN
          </h2>
          <p style="font-size: 21px; color: #334155; max-width: 800px; line-height: 1.6;">
            Các kíp trực y khoa thực hiện bốc thăm/tiếp nhận 3 hồ sơ ca bệnh (Nam, Linh, Hoàng) gặp các tình trạng mệt mỏi, mụn nhờn và béo phì tuổi dậy thì.
          </p>
          <button class="btn-action" style="font-size: 19px; padding: 16px 42px;" onclick="nextSlide()">[ BẮT ĐẦU TÁC NGHIỆP GIAI ĐOẠN 2 ➔ ]</button>
        </div>
      </div>
    </section>

    <!-- SLIDE 5 [GT02]: HOẠT ĐỘNG 1: GIỚI THIỆU (GĐ2) -->
    <section class="slide" id="slide-4">
      <h2 class="slide-title"><span class="tag">HOẠT ĐỘNG 1</span> TIẾP NHẬN CA BỆNH & BÁO ĐỘNG DINH DƯỠNG</h2>
      <div class="slide-body">
        <div style="font-size: 70px;">🚨</div>
        <h3 style="font-family: 'Montserrat', sans-serif; font-size: 36px; font-weight: 900; color: #DC2626; text-align: center;">🔴 BÁO ĐỘNG ĐỎ KHOA DINH DƯỠNG NOVA HOSPITAL</h3>
        <p style="font-size: 24px; max-width: 950px; color: #334155; text-align: center; line-height: 1.7;">
          Khoa Dinh dưỡng vừa tiếp nhận 3 ca bệnh cấp cứu của các bạn học sinh 12 tuổi đang gặp tình trạng kiệt sức, da sần mụn nhờn và tăng cân thất thường.
        </p>
        <button class="btn-action" style="font-size: 20px; padding: 18px 45px;" onclick="nextSlide()">[ XEM HƯỚNG DẪN TÁC NGHIỆP ➔ ]</button>
      </div>
    </section>

    <!-- SLIDE 6 [HD01]: HOẠT ĐỘNG 1: HƯỚNG DẪN 3 BƯỚC (GĐ2) -->
    <section class="slide" id="slide-5">
      <h2 class="slide-title"><span class="tag">HƯỚNG DẪN HĐ1</span> QUY TRÌNH 3 BƯỚC PHÂN TÍCH HỒ SƠ CA BỆNH</h2>
      <div class="slide-body">
        <div class="grid-3">
          <div class="card">
            <div class="card-title">📖 Bước 1: Đọc bệnh án</div>
            <div class="card-desc">Đọc kỹ 3 hồ sơ bệnh án của Nam, Linh và Hoàng được trình chiếu trên màn hình slide.</div>
          </div>
          <div class="card">
            <div class="card-title">💬 Bước 2: Thảo luận nhóm</div>
            <div class="card-desc">Thảo luận nhóm đôi trong kíp trực, đối chiếu triệu chứng và ghi các từ khóa thói quen có hại vào Sổ ghi chép.</div>
          </div>
          <div class="card">
            <div class="card-title">🖥️ Bước 3: Thao tác màn hình</div>
            <div class="card-desc">Đại diện các kíp trực lên bảng thao tác trực tiếp bấm chọn từ khóa thói quen xấu trên slide.</div>
          </div>
        </div>
        <div style="text-align: center; margin-top: 15px;">
          <button class="btn-action" style="font-size: 20px; padding: 18px 45px;" onclick="nextSlide()">[ SÃN SÀNG KHÁM BỆNH LÂM SÀNG ➔ ]</button>
        </div>
      </div>
    </section>

    <!-- SLIDE 7 [STAGE BANNER GĐ3]: KHÁM BỆNH LÂM SÀNG -->
    <section class="slide" id="slide-6">
      <div class="slide-body" style="justify-content: center; align-items: center; text-align: center;">
        <div class="banner-card">
          <div class="banner-stage-tag">🩺 CONCEPT BÁC SĨ NOVA HOSPITAL - GIAI ĐOẠN 3</div>
          <div style="font-size: 70px;">🩺</div>
          <h2 style="font-family: 'Montserrat', sans-serif; font-size: 38px; font-weight: 900; color: #0C4E4B;">
            GIAI ĐOẠN 3: KHÁM BỆNH LÂM SÀNG & GIẢI MÃ BỆNH ÁN
          </h2>
          <p style="font-size: 21px; color: #334155; max-width: 800px; line-height: 1.6;">
            Kíp trực tác nghiệp khám triệu chứng, truy tìm và chọn gạch chân đỏ các thói quen ăn uống sai lầm của 3 bệnh nhân trên màn hình slide.
          </p>
          <button class="btn-action" style="font-size: 19px; padding: 16px 42px;" onclick="nextSlide()">[ BẮT ĐẦU KHÁM BỆNH LÂM SÀNG ⏱️ ]</button>
        </div>
      </div>
    </section>

    <!-- SLIDE 8 [TH01]: HOẠT ĐỘNG 1: TRÒ CHƠI GIẢI MÃ BỆNH ÁN (GĐ3) -->
    <section class="slide" id="slide-7">
      <h2 class="slide-title">
        <span class="tag">THỰC HÀNH HĐ1</span> TRÒ CHƠI GIẢI MÃ THÓI QUEN BỆNH ÁN
        <span class="timer-box" style="margin-left: auto;">
          ⏱️ <span id="timer1">03:00</span>
          <button class="btn-timer-start" onclick="startTimer('timer1', 180)">▶ BẮT ĐẦU ĐẾM GIỜ</button>
        </span>
      </h2>
      <div class="slide-body">
        <p style="font-size: 17px; color: #0C4E4B; font-weight: 800; text-align: left; width: 100%;">
          👉 Bấm trực tiếp vào các từ ngữ thể hiện thói quen ăn uống sai lầm trong 3 hồ sơ bệnh án dưới đây:
        </p>
        <div class="grid-3">
          <div class="dossier-box">
            <div class="dossier-title">📁 Hồ sơ 1: Bệnh nhân Nam (12t)</div>
            <div class="dossier-content">
              Nam 12 tuổi, dạo này da mặt nổi mụn nhờn. Cậu có thói quen <span class="habit-kw" onclick="checkHabit(this)">nghiện trà sữa ngọt</span> và hay <span class="habit-kw" onclick="checkHabit(this)">thức khuya xem điện thoại</span>. Giờ học Nam hay mệt mỏi, thiếu tập trung.
            </div>
          </div>
          <div class="dossier-box">
            <div class="dossier-title">📁 Hồ sơ 2: Bệnh nhân Linh (12t)</div>
            <div class="dossier-content">
              Linh 12 tuổi, hay bị hoa mắt chóng mặt và chiều cao chậm phát triển so với các bạn. Linh có thói quen <span class="habit-kw" onclick="checkHabit(this)">thường xuyên bỏ bữa sáng</span> vì sợ trễ giờ học.
            </div>
          </div>
          <div class="dossier-box">
            <div class="dossier-title">📁 Hồ sơ 3: Bệnh nhân Hoàng (12t)</div>
            <div class="dossier-content">
              Hoàng 12 tuổi, tăng cân nhanh, có dấu hiệu béo phì nhưng cơ bắp lại yếu. Hoàng thích <span class="habit-kw" onclick="checkHabit(this)">ăn nhiều bánh kẹo ngọt</span> và rất <span class="habit-kw" onclick="checkHabit(this)">ngại uống nước lọc</span>.
            </div>
          </div>
        </div>
        <div style="text-align: center; margin-top: 10px;">
          <button class="btn-action" style="font-size: 18px; padding: 12px 35px;" onclick="nextSlide()">[ XEM ĐÁP ÁN & CHỐT BÀI ➔ ]</button>
        </div>
      </div>
    </section>

    <!-- SLIDE 9 [ĐA01]: HOẠT ĐỘNG 1: ĐÁP ÁN (GĐ3) -->
    <section class="slide" id="slide-8">
      <h2 class="slide-title"><span class="tag">ĐÁP ÁN HĐ1</span> NGUYÊN NHÂN TỔN HẠI THỂ CHẤT TUỔI DẬY THÌ</h2>
      <div class="slide-body">
        <div class="grid-3">
          <div class="card">
            <div class="card-title" style="color: #DC2626;">❌ Bỏ bữa sáng</div>
            <div class="card-desc">Thiếu đường trong máu (glucose) cho não bộ ➔ Mệt mỏi, hoa mắt, giảm khả năng tiếp thu bài học.</div>
          </div>
          <div class="card">
            <div class="card-title" style="color: #DC2626;">❌ Nghiện đồ ngọt & trà sữa</div>
            <div class="card-desc">Gây rối loạn hormone nội tiết ➔ Tích tụ mỡ béo phì, da tiết mồ hôi và nổi mụn trứng cá.</div>
          </div>
          <div class="card">
            <div class="card-title" style="color: #DC2626;">❌ Uống ít nước lọc</div>
            <div class="card-desc">Độc tố không thể đào thải ➔ Bề mặt da nhờn mụn, cơ thể uể uể thiếu sức sống.</div>
          </div>
        </div>
        <div style="background: #FEF3C7; border: 2px solid #D97706; padding: 18px 30px; border-radius: 20px; text-align: center; width: 100%;">
          <p style="font-size: 20px; font-weight: 800; color: #92400E;">
            📌 KẾT LUẬN SƯ PHẠM: Tuổi dậy thì là giai đoạn bứt phá thể chất vàng. Cần từ chối ngay các thói quen ăn uống sai lầm!
          </p>
        </div>
        <button class="btn-action" style="font-size: 19px; padding: 16px 42px;" onclick="nextSlide()">[ CHUYỂN SANG GIAI ĐOẠN 4 ➔ ]</button>
      </div>
    </section>

    <!-- SLIDE 10 [STAGE BANNER GĐ4]: CHẨN ĐOÁN NGUYÊN NHÂN -->
    <section class="slide" id="slide-9">
      <div class="slide-body" style="justify-content: center; align-items: center; text-align: center;">
        <div class="banner-card">
          <div class="banner-stage-tag">🩺 CONCEPT BÁC SĨ NOVA HOSPITAL - GIAI ĐOẠN 4</div>
          <div style="font-size: 70px;">🔬</div>
          <h2 style="font-family: 'Montserrat', sans-serif; font-size: 38px; font-weight: 900; color: #0C4E4B;">
            GIAI ĐOẠN 4: CHẨN ĐOÁN NGUYÊN NHÂN & HỘI CHẨN CHUYÊN KHOA
          </h2>
          <p style="font-size: 21px; color: #334155; max-width: 800px; line-height: 1.6;">
            Phân công 5 Bác sĩ chuyên khoa (Thần kinh, Cơ xương, Nội tiết, Cảm xúc, Da). Thảo luận kíp trực nghiên cứu nhu cầu sinh lý và giải pháp dưỡng chất tương ứng.
          </p>
          <button class="btn-action" style="font-size: 19px; padding: 16px 42px;" onclick="nextSlide()">[ BẮT ĐẦU CHẨN ĐOÁN CHUYÊN KHOA ➔ ]</button>
        </div>
      </div>
    </section>

    <!-- SLIDE 11 [GT03]: HOẠT ĐỘNG 2: GIỚI THIỆU (GĐ4) -->
    <section class="slide" id="slide-10">
      <h2 class="slide-title"><span class="tag">HOẠT ĐỘNG 2</span> KHÁM BỆNH & GIẢI MÃ MA TRẬN DƯỠNG CHẤT</h2>
      <div class="slide-body">
        <div style="font-size: 70px;">🔬</div>
        <h3 style="font-family: 'Montserrat', sans-serif; font-size: 34px; font-weight: 900; color: #0C4E4B; text-align: center;">
          HỘI CHẨN 5 BÁC SĨ CHUYÊN KHOA DINH DƯỠNG
        </h3>
        <p style="font-size: 22px; max-width: 900px; color: #334155; text-align: center; line-height: 1.7;">
          Hãy khám phá mối liên hệ trực tiếp giữa 5 Hệ cơ quan tuổi dậy thì và các Dưỡng chất thiết yếu để chẩn đoán phác đồ phục hồi!
        </p>
        <button class="btn-action" style="font-size: 20px; padding: 18px 45px;" onclick="nextSlide()">[ XEM HƯỚNG DẪN HỘI CHẨN ➔ ]</button>
      </div>
    </section>

    <!-- SLIDE 12 [HD02]: HOẠT ĐỘNG 2: HƯỚNG DẪN 3 BƯỚC (GĐ4) -->
    <section class="slide" id="slide-11">
      <h2 class="slide-title"><span class="tag">HƯỚNG DẪN HĐ2</span> QUY TRÌNH 3 BƯỚC KHÁM BỆNH & CHẠM NỐI MA TRẬN</h2>
      <div class="slide-body">
        <div class="grid-3">
          <div class="card">
            <div class="card-title">👨‍⚕️ Bước 1: Tiếp nhận chuyên khoa</div>
            <div class="card-desc">Lắng nghe phân công chẩn đoán theo các chuyên khoa (Thần kinh, Cơ xương, Nội tiết, Cảm xúc, Da).</div>
          </div>
          <div class="card">
            <div class="card-title">💬 Bước 2: Thảo luận kíp trực</div>
            <div class="card-desc">Các nhóm thảo luận, đối chiếu nhu cầu sinh lý từng hệ cơ quan và ghi chú giải pháp dưỡng chất vào Sổ ghi chép.</div>
          </div>
          <div class="card">
            <div class="card-title">🔗 Bước 3: Nối ma trận slide</div>
            <div class="card-desc">Đại diện kíp trực báo cáo chẩn đoán và lên bảng thực hiện chạm nối ma trận trên slide.</div>
          </div>
        </div>
        <div style="display: flex; gap: 15px; margin-top: 10px;">
          <button class="btn-header" style="font-size: 16px; padding: 12px 25px;" onclick="showModal('YÊU CẦU BÁC SĨ CHUYÊN KHOA 💡', '• Bác sĩ Thần kinh: Cần vi chất giúp não ghi nhớ tốt.<br>• Bác sĩ Cơ xương: Cần Canxi & Protein tăng chiều cao.<br>• Bác sĩ Da & Nội tiết: Cần Nước lọc sạch độc tố & hạn chế đồ ngọt.')">
            💡 XEM YÊU CẦU CHUYÊN KHOA
          </button>
          <button class="btn-action" style="font-size: 18px; padding: 14px 38px;" onclick="nextSlide()">[ CHUYỂN SANG GIAI ĐOẠN 5 ➔ ]</button>
        </div>
      </div>
    </section>

    <!-- SLIDE 13 [STAGE BANNER GĐ5]: HỘI CHẨN Y KHOA -->
    <section class="slide" id="slide-12">
      <div class="slide-body" style="justify-content: center; align-items: center; text-align: center;">
        <div class="banner-card">
          <div class="banner-stage-tag">🩺 CONCEPT BÁC SĨ NOVA HOSPITAL - GIAI ĐOẠN 5</div>
          <div style="font-size: 70px;">⚖️</div>
          <h2 style="font-family: 'Montserrat', sans-serif; font-size: 38px; font-weight: 900; color: #0C4E4B;">
            GIAI ĐOẠN 5: HỘI CHẨN Y KHOA TOÀN ĐOÀN & CHỐT KẾT LUẬN
          </h2>
          <p style="font-size: 21px; color: #334155; max-width: 800px; line-height: 1.6;">
            Đại diện các kíp trực lên bảng ghép nối Ma trận 5 Hệ cơ quan, Bác sĩ trưởng khoa chốt 3 Yếu tố Chế độ Dinh dưỡng & 3 Nguyên tắc Vàng.
          </p>
          <button class="btn-action" style="font-size: 19px; padding: 16px 42px;" onclick="nextSlide()">[ BẮT ĐẦU HỘI CHẨN NỐI MA TRẬN ⏱️ ]</button>
        </div>
      </div>
    </section>

    <!-- SLIDE 14 [TH02]: HOẠT ĐỘNG 2: GAME CHẠM NỐI MA TRẬN (GĐ5) -->
    <section class="slide" id="slide-13">
      <h2 class="slide-title">
        <span class="tag">THỰC HÀNH HĐ2</span> TRÒ CHƠI CHẠM NỐI MA TRẬN 5 HỆ CƠ QUAN
        <span class="timer-box" style="margin-left: auto;">
          ⏱️ <span id="timer2">05:00</span>
          <button class="btn-timer-start" onclick="startTimer('timer2', 300)">▶ BẮT ĐẦU ĐẾM GIỜ</button>
        </span>
      </h2>
      <div class="slide-body">
        <p style="font-size: 17px; color: #0C4E4B; font-weight: 800; text-align: left; width: 100%;">
          👉 Lần lượt bấm 1 thẻ ở Cột 1 (Hệ cơ quan), sau đó bấm 1 thẻ tương ứng ở Cột 2 (Dưỡng chất) để nối đáp án chuẩn:
        </p>
        <div class="matrix-container" id="matrixContainer">
          <svg id="matrixSvg"></svg>
          <div class="matrix-col" id="colSystem">
            <div class="matrix-item" data-id="1" onclick="clickMatrixLeft(this)">1. Hệ thần kinh (Não phát triển)</div>
            <div class="matrix-item" data-id="2" onclick="clickMatrixLeft(this)">2. Hệ cơ & xương (Tăng chiều cao)</div>
            <div class="matrix-item" data-id="3" onclick="clickMatrixLeft(this)">3. Hệ nội tiết & mồ hôi</div>
            <div class="matrix-item" data-id="4" onclick="clickMatrixLeft(this)">4. Cảm xúc tuổi dậy thì</div>
            <div class="matrix-item" data-id="5" onclick="clickMatrixLeft(this)">5. Hệ da (Nhờn & nổi mụn)</div>
          </div>
          <div class="matrix-col" id="colNutrient">
            <div class="matrix-item" data-id="A" onclick="clickMatrixRight(this)">A. Đạm Protein, Canxi, Vit D, Kẽm</div>
            <div class="matrix-item" data-id="B" onclick="clickMatrixRight(this)">B. Chất béo tốt Omega-3 & Vit B</div>
            <div class="matrix-item" data-id="C" onclick="clickMatrixRight(this)">C. Hạn chế đường, Sắt & Nước</div>
            <div class="matrix-item" data-id="D" onclick="clickMatrixRight(this)">D. Uống đủ 8-10 cốc nước/ngày</div>
            <div class="matrix-item" data-id="E" onclick="clickMatrixRight(this)">E. Ăn đa dạng nhóm chất + Ngủ đủ</div>
          </div>
        </div>
        <div style="text-align: center; margin-top: 15px;">
          <button class="btn-action" style="font-size: 18px; padding: 12px 35px;" onclick="nextSlide()">[ XEM ĐÁP ÁN & KẾT LUẬN HỘI CHẨN ➔ ]</button>
        </div>
      </div>
    </section>

    <!-- SLIDE 15 [ĐA02]: HOẠT ĐỘNG 2: ĐÁP ÁN (GĐ5) -->
    <section class="slide" id="slide-14">
      <h2 class="slide-title"><span class="tag">TỔNG KẾT HĐ2</span> TỔNG KẾT KIẾN THỨC CỐT LÕI</h2>
      <div class="slide-body">
        <div class="grid-2">
          <div class="card" style="min-height: 250px;">
            <div class="card-title">📌 3 YẾU TỐ CHẾ ĐỘ DINH DƯỠNG</div>
            <div class="card-desc" style="font-size: 18px;">
              • <strong>Nhóm chất:</strong> Ăn đa dạng các loại thực phẩm trong các nhóm chất.<br>
              • <strong>Lượng thức ăn:</strong> Cân đối giữa các nhóm thực phẩm trên Đĩa ăn.<br>
              • <strong>Thời điểm ăn:</strong> Ăn đúng giờ, đủ 3 bữa chính, 1-2 bữa phụ.
            </div>
          </div>
          <div class="card" style="min-height: 250px;">
            <div class="card-title">📌 3 NGUYÊN TẮC DINH DƯỠNG TUỔI DẬY THÌ</div>
            <div class="card-desc" style="font-size: 18px;">
              • <strong>Đa dạng & Cân đối:</strong> Cung cấp đủ đạm, canxi, chất béo tốt.<br>
              • <strong>Bổ sung Đạm & Canxi & Nước:</strong> Uống đủ 8-10 cốc nước/ngày.<br>
              • <strong>Hạn chế đồ ngọt:</strong> Giảm trà sữa, nước có ga & bánh kẹo.
            </div>
          </div>
        </div>
        <div style="text-align: center; margin-top: 15px;">
          <button class="btn-action" style="font-size: 19px; padding: 16px 42px;" onclick="nextSlide()">[ SANG GIAI ĐOẠN 6: KÊ ĐƠN PHÁC ĐỒ ➔ ]</button>
        </div>
      </div>
    </section>

    <!-- SLIDE 16 [STAGE BANNER GĐ6]: KÊ ĐƠN PHÁC ĐỒ -->
    <section class="slide" id="slide-15">
      <div class="slide-body" style="justify-content: center; align-items: center; text-align: center;">
        <div class="banner-card">
          <div class="banner-stage-tag">🩺 CONCEPT BÁC SĨ NOVA HOSPITAL - GIAI ĐOẠN 6</div>
          <div style="font-size: 70px;">⚡</div>
          <h2 style="font-family: 'Montserrat', sans-serif; font-size: 38px; font-weight: 900; color: #0C4E4B;">
            GIAI ĐOẠN 6: KÊ ĐƠN PHÁC ĐỒ & KÍCH HOẠT TRẠM DƯỠNG CHẤT
          </h2>
          <p style="font-size: 21px; color: #334155; max-width: 800px; line-height: 1.6;">
            Thao tác Kéo & Thả vi chất lành mạnh nạp đầy 100% Thanh năng lượng cho 3 Trạm Dưỡng chất (Thần kinh, Cơ xương, Da & Nội tiết).
          </p>
          <button class="btn-action" style="font-size: 19px; padding: 16px 42px;" onclick="nextSlide()">[ BẮT ĐẦU KÍCH HOẠT TRẠM DƯỠNG CHẤT ➔ ]</button>
        </div>
      </div>
    </section>

    <!-- SLIDE 17 [GT04]: HOẠT ĐỘNG 3: GIỚI THIỆU (GĐ6) -->
    <section class="slide" id="slide-16">
      <h2 class="slide-title"><span class="tag">HOẠT ĐỘNG 3</span> KÊ ĐƠN PHÁC ĐỒ & KÍCH HOẠT TRẠM DƯỠNG CHẤT</h2>
      <div class="slide-body">
        <div style="font-size: 70px;">🍱</div>
        <h3 style="font-family: 'Montserrat', sans-serif; font-size: 34px; font-weight: 900; color: #0C4E4B; text-align: center;">
          MÔ HÌNH 3 TRẠM DƯỠNG CHẤT TRỌNG ĐIỂM
        </h3>
        <p style="font-size: 22px; max-width: 900px; color: #334155; text-align: center; line-height: 1.7;">
          Lựa chọn thực phẩm vàng bổ sung dinh dưỡng chuyên biệt cho 3 hệ cơ quan mục tiêu: Thần kinh (Não bộ), Cơ xương (Chiều cao), Da & Nội tiết.
        </p>
        <button class="btn-action" style="font-size: 20px; padding: 18px 45px;" onclick="nextSlide()">[ XEM HƯỚNG DẪN 3 TRẠM ➔ ]</button>
      </div>
    </section>

    <!-- SLIDE 18 [HD03]: HOẠT ĐỘNG 3: HƯỚNG DẪN 3 BƯỚC (GĐ6) -->
    <section class="slide" id="slide-17">
      <h2 class="slide-title"><span class="tag">HƯỚNG DẪN HĐ3</span> QUY TRÌNH 3 BƯỚC KÍCH HOẠT TRẠM DƯỠNG CHẤT</h2>
      <div class="slide-body">
        <div class="grid-3">
          <div class="card">
            <div class="card-title">🔍 Bước 1: Nghiên cứu vi chất</div>
            <div class="card-desc">Quan sát mô hình 3 Trạm Dưỡng chất trên slide và kiểm tra danh mục thực phẩm.</div>
          </div>
          <div class="card">
            <div class="card-title">📝 Bước 2: Kê đơn phiếu A4</div>
            <div class="card-desc">Kíp trực thảo luận, dán/điền thực phẩm lành mạnh vào 3 Trạm Dưỡng chất trên Phiếu in A4.</div>
          </div>
          <div class="card">
            <div class="card-title">⚡ Bước 3: Nạp 100% năng lượng</div>
            <div class="card-desc">Đại diện kíp trực lên bảng kéo - thả thẻ vi chất nạp năng lượng tăng dần tích lũy đến 100%.</div>
          </div>
        </div>
        <div style="text-align: center; margin-top: 15px;">
          <button class="btn-action" style="font-size: 20px; padding: 18px 45px;" onclick="nextSlide()">[ BẮT ĐẦU GAME KÍCH HOẠT TRẠM ⏱️ ]</button>
        </div>
      </div>
    </section>

    <!-- SLIDE 19 [TH03]: HOẠT ĐỘNG 3: GAME DRAG & DROP (GĐ6) -->
    <section class="slide" id="slide-18">
      <h2 class="slide-title">
        <span class="tag">THỰC HÀNH HĐ3</span> TRÒ CHƠI KÍCH HOẠT TRẠM DƯỠNG CHẤT 3 HỆ CƠ QUAN
        <span class="timer-box" style="margin-left: auto;">
          ⏱️ <span id="timer3">05:00</span>
          <button class="btn-timer-start" onclick="startTimer('timer3', 300)">▶ BẮT ĐẦU ĐẾM GIỜ</button>
        </span>
      </h2>
      <div class="slide-body">
        <div style="display: flex; gap: 25px; align-items: flex-start; width: 100%;">
          <div class="station-container">
            <div class="station-card" id="st-than-kinh" ondragover="allowDrop(event)" ondragleave="leaveDrop(event)" ondrop="dropNutrient(event, 'than-kinh')">
              <div class="station-title">
                <span>🧠 TRẠM DƯỠNG THẦN KINH (NÃO BỘ)</span>
                <span style="font-size: 14px; color: #0F766E;" id="percent-than-kinh">0%</span>
              </div>
              <div class="station-progress-bg">
                <div class="station-progress-bar" id="bar-than-kinh"></div>
              </div>
              <div class="food-tag-container" id="tag-than-kinh"></div>
            </div>

            <div class="station-card" id="st-co-xuong" ondragover="allowDrop(event)" ondragleave="leaveDrop(event)" ondrop="dropNutrient(event, 'co-xuong')">
              <div class="station-title">
                <span>🦴 TRẠM DƯỠNG CƠ XƯƠNG (XƯƠNG KHỚP)</span>
                <span style="font-size: 14px; color: #0F766E;" id="percent-co-xuong">0%</span>
              </div>
              <div class="station-progress-bg">
                <div class="station-progress-bar" id="bar-co-xuong"></div>
              </div>
              <div class="food-tag-container" id="tag-co-xuong"></div>
            </div>

            <div class="station-card" id="st-da-noi-tiet" ondragover="allowDrop(event)" ondragleave="leaveDrop(event)" ondrop="dropNutrient(event, 'da-noi-tiet')">
              <div class="station-title">
                <span>✨ TRẠM DƯỠNG DA & NỘI TIẾT (LÀN DA & HORMONE)</span>
                <span style="font-size: 14px; color: #0F766E;" id="percent-da-noi-tiet">0%</span>
              </div>
              <div class="station-progress-bg">
                <div class="station-progress-bar" id="bar-da-noi-tiet"></div>
              </div>
              <div class="food-tag-container" id="tag-da-noi-tiet"></div>
            </div>
          </div>

          <div style="flex: 1;">
            <p style="font-size: 17px; color: #0C4E4B; font-weight: 800; margin-bottom: 10px;">
              👉 Kéo & thả (hoặc click chọn) các thẻ vi chất độc lập vào đúng 3 Trạm Dưỡng chất để nạp năng lượng 100%:
            </p>
            <div class="food-pantry" id="food-pantry-container">
              <div class="food-chip" draggable="true" id="c1" data-target="than-kinh" data-name="🐟 Cá hồi" ondragstart="dragStart(event)" onclick="clickNutrientCard(this)">🐟 Cá hồi</div>
              <div class="food-chip" draggable="true" id="c2" data-target="co-xuong" data-name="🥛 Sữa tươi" ondragstart="dragStart(event)" onclick="clickNutrientCard(this)">🥛 Sữa tươi</div>
              <div class="food-chip" draggable="true" id="c3" data-target="da-noi-tiet" data-name="🚰 Nước lọc" ondragstart="dragStart(event)" onclick="clickNutrientCard(this)">🚰 Nước lọc</div>
              <div class="food-chip" draggable="true" id="c4" data-target="bad" data-name="🥤 Trà sữa trân châu" ondragstart="dragStart(event)" onclick="clickNutrientCard(this)">🥤 Trà sữa trân châu</div>
              <div class="food-chip" draggable="true" id="c5" data-target="than-kinh" data-name="🌰 Hạt óc chó" ondragstart="dragStart(event)" onclick="clickNutrientCard(this)">🌰 Hạt óc chó</div>
              <div class="food-chip" draggable="true" id="c6" data-target="co-xuong" data-name="🦐 Tôm biển" ondragstart="dragStart(event)" onclick="clickNutrientCard(this)">🦐 Tôm biển</div>
              <div class="food-chip" draggable="true" id="c7" data-target="da-noi-tiet" data-name="🍊 Quả cam" ondragstart="dragStart(event)" onclick="clickNutrientCard(this)">🍊 Quả cam</div>
              <div class="food-chip" draggable="true" id="c8" data-target="bad" data-name="🍗 Gà rán chiên dầu" ondragstart="dragStart(event)" onclick="clickNutrientCard(this)">🍗 Gà rán chiên dầu</div>
              <div class="food-chip" draggable="true" id="c9" data-target="than-kinh" data-name="🥚 Trứng gà" ondragstart="dragStart(event)" onclick="clickNutrientCard(this)">🥚 Trứng gà</div>
              <div class="food-chip" draggable="true" id="c10" data-target="co-xuong" data-name="🥦 Bông cải" ondragstart="dragStart(event)" onclick="clickNutrientCard(this)">🥦 Bông cải</div>
              <div class="food-chip" draggable="true" id="c11" data-target="da-noi-tiet" data-name="🍧 Sữa chua" ondragstart="dragStart(event)" onclick="clickNutrientCard(this)">🍧 Sữa chua</div>
              <div class="food-chip" draggable="true" id="c12" data-target="bad" data-name="🍬 Kẹo ngọt" ondragstart="dragStart(event)" onclick="clickNutrientCard(this)">🍬 Kẹo ngọt</div>
              <div class="food-chip" draggable="true" id="c13" data-target="than-kinh" data-name="🌾 Ngũ cốc" ondragstart="dragStart(event)" onclick="clickNutrientCard(this)">🌾 Ngũ cốc</div>
              <div class="food-chip" draggable="true" id="c14" data-target="co-xuong" data-name="🥩 Thịt nạc" ondragstart="dragStart(event)" onclick="clickNutrientCard(this)">🥩 Thịt nạc</div>
              <div class="food-chip" draggable="true" id="c15" data-target="da-noi-tiet" data-name="🥑 Quả bơ" ondragstart="dragStart(event)" onclick="clickNutrientCard(this)">🥑 Quả bơ</div>
              <div class="food-chip" draggable="true" id="c16" data-target="bad" data-name="🍟 Khoai tây chiên" ondragstart="dragStart(event)" onclick="clickNutrientCard(this)">🍟 Khoai tây chiên</div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- SLIDE 20 [ĐA03]: HOẠT ĐỘNG 3: ĐÁP ÁN (GĐ6) -->
    <section class="slide" id="slide-19">
      <h2 class="slide-title"><span class="tag">ĐÁP ÁN HĐ3</span> PHÁC ĐỒ BỔ SUNG DƯỠNG CHẤT 3 HỆ CƠ QUAN</h2>
      <div class="slide-body">
        <div class="grid-3">
          <div class="card" style="min-height: 230px;">
            <div class="card-title" style="color: #D97706;">🧠 PHÁC ĐỒ THẦN KINH (NÃO BỘ)</div>
            <div class="card-desc">• Cá hồi, Hạt óc chó, Trứng gà, Ngũ cốc nguyên hạt.<br>• Vi chất: Omega-3, Choline & Vitamin B.<br>• Tác dụng: Tăng độ tập trung, ghi nhớ bài học tốt.</div>
          </div>
          <div class="card" style="min-height: 230px;">
            <div class="card-title" style="color: #DC2626;">🦴 PHÁC ĐỒ CƠ XƯƠNG (XƯƠNG KHỚP)</div>
            <div class="card-desc">• Sữa tươi, Tôm, Bông cải xanh, Thịt nạc.<br>• Vi chất: Canxi, Vitamin D3 & Protein.<br>• Tác dụng: Thúc đẩy chiều cao bứt phá, xương vững chắc.</div>
          </div>
          <div class="card" style="min-height: 230px;">
            <div class="card-title" style="color: #059669;">✨ PHÁC ĐỒ DA & NỘI TIẾT</div>
            <div class="card-desc">• Nước lọc 8-10 cốc/ngày, Quả cam/Ổi, Sữa chua.<br>• Vi chất: Nước lọc sạch độc tố, Vitamin C & E.<br>• Tác dụng: Cân bằng hormone, da sạch mụn.</div>
          </div>
        </div>
        <div style="text-align: center; margin-top: 15px;">
          <button class="btn-stamp" style="font-size: 19px; padding: 16px 36px;" onclick="playStampSound(); showModal('ĐÃ THẨM ĐỊNH Y KHOA! 🏆', 'Phác đồ bổ sung dưỡng chất cho 3 hệ cơ quan đã được phê duyệt đạt 100% chuẩn Y khoa tuổi dậy thì!')">
            💮 ĐÓNG DẤU THẨM ĐỊNH Y KHOA
          </button>
        </div>
      </div>
    </section>

    <!-- SLIDE 21 [STAGE BANNER GĐ7]: NHẬT KÝ BÁC SĨ & CAM KẾT (GĐ7) -->
    <section class="slide" id="slide-20">
      <h2 class="slide-title"><span class="tag">GIAI ĐOẠN 7</span> NHẬT KÝ BÁC SĨ & BẢNG CAM KẾT DINH DƯỠNG CÁ NHÂN A4</h2>
      <div class="slide-body">
        <div class="grid-2">
          <div class="mindmap-node">
            <div class="mindmap-header">🧠 Sơ đồ tư duy 3 nhánh</div>
            <p class="card-desc" style="font-size: 16px;">
              • 3 Yếu tố Chế độ Dinh dưỡng (Nhóm chất, Lượng, Thời điểm)<br>
              • 5 Hệ cơ quan (Thần kinh, Cơ xương, Nội tiết, Cảm xúc, Da)<br>
              • 3 Nguyên tắc Vàng (Đa dạng, Bổ sung Canxi/Đạm/Nước, Hạn chế đồ ngọt)
            </p>
          </div>
          <div style="display: flex; flex-direction: column; gap: 10px; width: 100%;">
            <p style="font-size: 17px; color: #0C4E4B; font-weight: 800;">👉 Bấm chọn lời cam kết tự viết vào Giấy A4 cá nhân:</p>
            <div class="habit-item" onclick="toggleHabit(this)"><div class="checkbox-icon">✓</div><div>Ăn đầy đủ 3 bữa chính, không bao giờ bỏ bữa sáng.</div></div>
            <div class="habit-item" onclick="toggleHabit(this)"><div class="checkbox-icon">✓</div><div>Uống đủ 8 - 10 cốc nước lọc mỗi ngày để sáng da.</div></div>
            <div class="habit-item" onclick="toggleHabit(this)"><div class="checkbox-icon">✓</div><div>Hạn chế trà sữa, đồ ngọt, nước có ga & đồ chiên mỡ.</div></div>
            <div class="habit-item" onclick="toggleHabit(this)"><div class="checkbox-icon">✓</div><div>Tăng cường Đạm (thịt, cá, trứng) & Canxi (sữa).</div></div>
          </div>
        </div>
        <div style="text-align: center; margin-top: 10px;">
          <button class="btn-action" style="font-size: 19px; padding: 16px 42px;" onclick="nextSlide()">[ CHUYỂN SANG GIAI ĐOẠN 8 VINH DANH 🏆 ]</button>
        </div>
      </div>
    </section>

    <!-- SLIDE 22 [STAGE BANNER GĐ8]: THÓI QUEN KHỎE MẠNH & VINH DANH (GĐ8) -->
    <section class="slide" id="slide-21">
      <h2 class="slide-title"><span class="tag">GIAI ĐOẠN 8</span> THÓI QUEN KHỎE MẠNH & TRAO BẰNG BÁC SĨ NỘI TRÚ</h2>
      <div class="slide-body">
        <div class="cert-card">
          <div style="font-size: 60px; margin-bottom: 10px;">🎖️</div>
          <h2 class="cert-title">BẰNG VINH DANH BÁC SĨ DINH DƯỠNG NỘI TRÚ</h2>
          <p style="font-size: 24px; color: #334155; margin: 18px 0; font-weight: 500;">
            Trao tặng Kíp trực Bác sĩ tập sự Lớp 6 đã xuất sắc hoàn thành đào tạo:
          </p>
          <h3 style="font-family: 'Montserrat', sans-serif; font-size: 36px; font-weight: 900; color: #0C4E4B; margin-bottom: 24px;">
            THỰC ĐƠN VÀNG CHO TUỔI DẬY THÌ
          </h3>
          <p style="font-size: 20px; color: #475569; font-weight: 700;">Khoa Dinh dưỡng - Bệnh viện Nova Hospital 2026</p>
        </div>
        <button class="btn-action" style="font-size: 20px; padding: 18px 45px;" onclick="triggerConfetti(); playFanfareSound();">
          🎉 BẮN PHÁO HOA CHÚC MỪNG GIAI ĐOẠN 8
        </button>
      </div>
    </section>

  </main>

  <!-- Footer -->
  <footer>
    <button class="btn-nav" id="btnPrev" onclick="prevSlide()">◀ TRƯỚC</button>
    <div class="slide-counter" id="slideCounter">Slide 1 / 22</div>
    <span class="key-hint">💡 Phím ← và → trên bàn phím để chuyển slide</span>
    <button class="btn-nav" id="btnNext" onclick="nextSlide()">SAU ▶</button>
  </footer>
</div>

<!-- Drawer Menu -->
<div class="drawer-overlay" id="drawerOverlay" onclick="toggleDrawer()"></div>
<div class="drawer" id="drawer">
  <div class="drawer-header">
    <span class="drawer-title">DANH SÁCH SLIDE (22)</span>
    <button style="background: none; border: none; color: #DC2626; font-size: 24px; cursor: pointer;" onclick="toggleDrawer()">✕</button>
  </div>
  <div class="drawer-list" id="drawerList"></div>
</div>

<!-- Modal Glassmorphism -->
<div class="modal-overlay" id="customModal">
  <div class="modal-card">
    <div style="font-size: 60px;" id="modalIcon">💡</div>
    <h3 style="font-family: 'Montserrat', sans-serif; font-size: 26px; font-weight: 900; color: #0C4E4B;" id="modalTitle">THÔNG BÁO Y KHOA</h3>
    <div style="font-size: 18px; color: #334155; line-height: 1.7; text-align: center;" id="modalDesc">Nội dung thông báo</div>
    <button class="btn-action" style="font-size: 16px; padding: 12px 35px;" onclick="closeModal()">ĐÓNG THÔNG BÁO</button>
  </div>
</div>

<script>
  let currentSlide = 0;
  const totalSlides = 22;
  let timerIntervals = {};
  let foundHabitsCount = 0;

  const stages = [
    "Khoa Dinh dưỡng - Nova Hospital",
    "Giai đoạn 1: Mở khóa ca bệnh",
    "Giai đoạn 1: Nhiệm vụ bài học",
    "Giai đoạn 2: Nhận hồ sơ bệnh án",
    "Giai đoạn 2: Báo động dinh dưỡng",
    "Giai đoạn 2: Hướng dẫn 3 bước",
    "Giai đoạn 3: Khám bệnh lâm sàng",
    "Giai đoạn 3: Game Giải mã thói quen",
    "Giai đoạn 3: Đáp án HĐ1",
    "Giai đoạn 4: Chẩn đoán nguyên nhân",
    "Giai đoạn 4: Giới thiệu HĐ2",
    "Giai đoạn 4: Hướng dẫn 3 bước",
    "Giai đoạn 5: Hội chẩn y khoa",
    "Giai đoạn 5: Game Chạm nối Ma trận",
    "Giai đoạn 5: Chốt 3 yếu tố + 3 nguyên tắc",
    "Giai đoạn 6: Kê đơn phác đồ",
    "Giai đoạn 6: Mô hình 3 Trạm Dưỡng chất",
    "Giai đoạn 6: Hướng dẫn 3 bước",
    "Giai đoạn 6: Drag & Drop Nạp 100%",
    "Giai đoạn 6: Đáp án Phác đồ thẩm định",
    "Giai đoạn 7: Nhật ký bác sĩ & Cam kết A4",
    "Giai đoạn 8: Thói quen khỏe mạnh & Vinh danh"
  ];

  const slideTitles = [
    "1. Mở đầu bài học",
    "2. GĐ1: Mục tiêu bài học (K-S-A)",
    "3. GĐ1: Nhiệm vụ bài học",
    "4. GĐ2: Banner Nhận hồ sơ bệnh án",
    "5. GĐ2: Hoạt động 1: Báo động dinh dưỡng",
    "6. GĐ2: Hoạt động 1: Hướng dẫn 3 bước",
    "7. GĐ3: Banner Khám bệnh lâm sàng",
    "8. GĐ3: Hoạt động 1: Game Giải mã Bệnh án",
    "9. GĐ3: Hoạt động 1: Đáp án & Chốt bài HĐ1",
    "10. GĐ4: Banner Chẩn đoán nguyên nhân",
    "11. GĐ4: Hoạt động 2: Giới thiệu Hoạt động 2",
    "12. GĐ4: Hoạt động 2: Hướng dẫn ghép nối Dưỡng chất",
    "13. GĐ5: Banner Hội chẩn y khoa toàn đoàn",
    "14. GĐ5: Hoạt động 2: Game Chạm nối Ma trận 5 hệ",
    "15. GĐ5: Hoạt động 2: Đáp án & Chốt kiến thức",
    "16. GĐ6: Banner Kê đơn phác đồ & Kích hoạt Trạm",
    "17. GĐ6: Hoạt động 3: Giới thiệu Mô hình 3 Trạm",
    "18. GĐ6: Hoạt động 3: Hướng dẫn Quy trình 3 bước",
    "19. GĐ6: Hoạt động 3: Game Drag & Drop (100%)",
    "20. GĐ6: Hoạt động 3: Đáp án Phác đồ 3 Hệ cơ quan",
    "21. GĐ7: Sơ đồ tư duy & Bảng cam kết cá nhân A4",
    "22. GĐ8: Vinh danh & Trao Bằng Bác sĩ Nội trú"
  ];

  // Audio Synth Engine
  function playSound(freq, duration, type='sine') {
    try {
      const ctx = new (window.AudioContext || window.webkitAudioContext)();
      const osc = ctx.createOscillator();
      const gain = ctx.createGain();
      osc.type = type;
      osc.frequency.setValueAtTime(freq, ctx.currentTime);
      gain.gain.setValueAtTime(0.15, ctx.currentTime);
      gain.gain.exponentialRampToValueAtTime(0.001, ctx.currentTime + duration);
      osc.connect(gain);
      gain.connect(ctx.destination);
      osc.start();
      osc.stop(ctx.currentTime + duration);
    } catch(e) {}
  }

  function playClick() { playSound(600, 0.08); }
  function playBeep() { playSound(400, 0.15, 'triangle'); }
  function playStampSound() { playSound(800, 0.25, 'square'); }
  function playFanfareSound() {
    [523.25, 659.25, 783.99, 1046.50].forEach((freq, i) => {
      setTimeout(() => playSound(freq, 0.35, 'triangle'), i * 120);
    });
  }

  // Timer logic
  function startTimer(id, seconds) {
    playClick();
    if (timerIntervals[id]) clearInterval(timerIntervals[id]);

    let display = document.getElementById(id);
    let rem = seconds;

    timerIntervals[id] = setInterval(() => {
      let m = Math.floor(rem / 60);
      let s = rem % 60;
      display.innerText = `${m < 10 ? '0' : ''}${m}:${s < 10 ? '0' : ''}${s}`;

      if (rem <= 0) {
        clearInterval(timerIntervals[id]);
        playFanfareSound();
        showModal('HẾT GIỜ TÁC NGHIỆP! ⏰', 'Đã hết thời gian dành cho hoạt động! Mời các kíp trực dừng tay và chuẩn bị báo cáo!');
      }
      rem--;
    }, 1000);
  }

  function checkHabit(el) {
    if (!el.classList.contains('found')) {
      playClick();
      el.classList.add('found');
      foundHabitsCount++;
      if (foundHabitsCount >= 4) {
        setTimeout(() => {
          playFanfareSound();
          showModal('XUẤT SẮC! 🎉', 'Kíp trực đã phát hiện chính xác tất cả các thói quen ăn uống sai lầm tổn hại sức khỏe!');
        }, 400);
      }
    }
  }

  // Game 2 Connecting SVG logic
  let matrixState = { left: null, right: null, matches: [] };
  const correctMatches = { '1': 'B', '2': 'A', '3': 'C', '4': 'E', '5': 'D' };

  function clickMatrixLeft(el) {
    if (el.classList.contains('matched')) return;
    playClick();
    document.querySelectorAll('#colSystem .matrix-item').forEach(i => i.classList.remove('selected'));
    el.classList.add('selected');
    matrixState.left = el;
    checkMatrixPair();
  }

  function clickMatrixRight(el) {
    if (el.classList.contains('matched')) return;
    playClick();
    document.querySelectorAll('#colNutrient .matrix-item').forEach(i => i.classList.remove('selected'));
    el.classList.add('selected');
    matrixState.right = el;
    checkMatrixPair();
  }

  function checkMatrixPair() {
    if (matrixState.left && matrixState.right) {
      const leftId = matrixState.left.getAttribute('data-id');
      const rightId = matrixState.right.getAttribute('data-id');

      if (correctMatches[leftId] === rightId) {
        playStampSound();
        matrixState.left.classList.remove('selected');
        matrixState.right.classList.remove('selected');
        matrixState.left.classList.add('matched');
        matrixState.right.classList.add('matched');

        drawSvgLine(matrixState.left, matrixState.right);
        matrixState.matches.push({ left: matrixState.left, right: matrixState.right });

        matrixState.left = null;
        matrixState.right = null;

        if (matrixState.matches.length === 5) {
          setTimeout(() => {
            playFanfareSound();
            showModal('GHÉP NỐI THÀNH CÔNG 100%! 🏆', 'Các kíp trực đã hoàn thành chính xác 100% Ma trận Dưỡng chất cho 5 Hệ cơ quan!');
          }, 400);
        }
      } else {
        playBeep();
        matrixState.left.classList.remove('selected');
        matrixState.right.classList.remove('selected');
        matrixState.left = null;
        matrixState.right = null;
      }
    }
  }

  function drawSvgLine(elLeft, elRight) {
    const svg = document.getElementById('matrixSvg');
    const container = document.getElementById('matrixContainer').getBoundingClientRect();
    const r1 = elLeft.getBoundingClientRect();
    const r2 = elRight.getBoundingClientRect();

    const x1 = r1.right - container.left;
    const y1 = r1.top + r1.height / 2 - container.top;
    const x2 = r2.left - container.left;
    const y2 = r2.top + r2.height / 2 - container.top;

    const line = document.createElementNS('http://www.w3.org/2000/svg', 'line');
    line.setAttribute('x1', x1);
    line.setAttribute('y1', y1);
    line.setAttribute('x2', x2);
    line.setAttribute('y2', y2);
    line.setAttribute('stroke', '#059669');
    line.setAttribute('stroke-width', '4.5');
    line.setAttribute('stroke-dasharray', '8 4');

    svg.appendChild(line);
  }

  function redrawLines() {
    const svg = document.getElementById('matrixSvg');
    if (!svg) return;
    svg.innerHTML = '';
    matrixState.matches.forEach(m => drawSvgLine(m.left, m.right));
  }

  window.addEventListener('resize', redrawLines);

  // HĐ3 Drag & Drop
  let stationProgress = { 'than-kinh': 0, 'co-xuong': 0, 'da-noi-tiet': 0 };

  function dragStart(e) {
    e.dataTransfer.setData("text/plain", e.target.id);
    e.dataTransfer.effectAllowed = "move";
  }

  function allowDrop(e) {
    e.preventDefault();
    e.currentTarget.classList.add('drag-over');
  }

  function leaveDrop(e) {
    e.currentTarget.classList.remove('drag-over');
  }

  function dropNutrient(e, stationId) {
    e.preventDefault();
    e.currentTarget.classList.remove('drag-over');
    const cardId = e.dataTransfer.getData("text/plain");
    const card = document.getElementById(cardId);
    if (card) processNutrientDrop(card, stationId);
  }

  function clickNutrientCard(cardEl) {
    if (cardEl.classList.contains('disabled')) return;
    const target = cardEl.getAttribute('data-target');
    if (target === 'bad') {
      processNutrientDrop(cardEl, 'than-kinh');
    } else {
      processNutrientDrop(cardEl, target);
    }
  }

  function processNutrientDrop(cardEl, stationId) {
    if (cardEl.classList.contains('disabled')) return;

    const targetStation = cardEl.getAttribute('data-target');
    const foodName = cardEl.getAttribute('data-name');
    const stationCard = document.getElementById(`st-${stationId}`);

    if (targetStation === 'bad' || targetStation !== stationId) {
      playBeep();
      if (stationCard) {
        stationCard.classList.remove('flash-red-anim', 'flash-green-anim');
        void stationCard.offsetWidth;
        stationCard.classList.add('flash-red-anim');
      }
      cardEl.classList.remove('card-snapback-anim');
      void cardEl.offsetWidth;
      cardEl.classList.add('card-snapback-anim');

      setTimeout(() => {
        if (stationCard) stationCard.classList.remove('flash-red-anim');
        cardEl.classList.remove('card-snapback-anim');
      }, 600);
      return;
    }

    playStampSound();
    cardEl.classList.add('disabled');

    if (stationCard) {
      stationCard.classList.remove('flash-red-anim', 'flash-green-anim');
      void stationCard.offsetWidth;
      stationCard.classList.add('flash-green-anim');
      setTimeout(() => {
        stationCard.classList.remove('flash-green-anim');
      }, 600);
    }

    stationProgress[stationId] = Math.min(100, stationProgress[stationId] + 25);
    const currentProgress = stationProgress[stationId];

    const bar = document.getElementById(`bar-${stationId}`);
    const percentText = document.getElementById(`percent-${stationId}`);
    const tagContainer = document.getElementById(`tag-${stationId}`);

    if (bar && percentText && tagContainer) {
      bar.style.width = `${currentProgress}%`;
      const newTag = document.createElement('div');
      newTag.className = 'food-tag-station';
      newTag.innerText = foodName;
      tagContainer.appendChild(newTag);

      if (currentProgress >= 100) {
        if (stationCard) stationCard.classList.add('filled');
        percentText.innerText = '100% ⚡ NẠP ĐẦY';
        percentText.style.color = '#059669';
        percentText.style.fontWeight = '900';
      } else {
        percentText.innerText = `${currentProgress}% ⚡`;
      }

      if (stationProgress['than-kinh'] >= 100 && stationProgress['co-xuong'] >= 100 && stationProgress['da-noi-tiet'] >= 100) {
        setTimeout(() => {
          triggerConfetti();
          playFanfareSound();
          showModal('KÍCH HOẠT THÀNH CÔNG 100%! ⚡🏆', 'Xuất sắc! Cả 3 Trạm Dưỡng Chất (Thần kinh, Cơ xương, Da & Nội tiết) đã được nạp đầy 100% năng lượng chuẩn Y khoa!', '🎉');
        }, 500);
      }
    }
  }

  function toggleHabit(el) {
    playBeep();
    el.classList.toggle('checked');
  }

  // Navigation Logic
  function goToSlide(index) {
    if (index < 0 || index >= totalSlides) return;
    playClick();

    document.querySelectorAll('.slide').forEach((s, idx) => {
      s.classList.toggle('active', idx === index);
    });

    currentSlide = index;

    document.getElementById('slideCounter').innerText = `Slide ${currentSlide + 1} / ${totalSlides}`;
    document.getElementById('stageBadge').innerText = stages[currentSlide] || 'Khoa Dinh dưỡng';
    document.getElementById('btnPrev').disabled = (currentSlide === 0);
    document.getElementById('btnNext').disabled = (currentSlide === totalSlides - 1);

    renderDrawerList();
    if (currentSlide === 13) {
      setTimeout(redrawLines, 100);
    }
    if (currentSlide === 21) { triggerConfetti(); playFanfareSound(); }
  }

  function nextSlide() { goToSlide(currentSlide + 1); }
  function prevSlide() { goToSlide(currentSlide - 1); }

  window.addEventListener('keydown', (e) => {
    if (e.key === 'ArrowRight') nextSlide();
    if (e.key === 'ArrowLeft') prevSlide();
  });

  function toggleDrawer() {
    document.getElementById('drawer').classList.toggle('open');
    document.getElementById('drawerOverlay').classList.toggle('open');
  }

  function renderDrawerList() {
    const list = document.getElementById('drawerList');
    list.innerHTML = '';
    slideTitles.forEach((title, idx) => {
      const item = document.createElement('div');
      item.className = `drawer-item ${idx === currentSlide ? 'active' : ''}`;
      item.innerText = title;
      item.onclick = () => { goToSlide(idx); toggleDrawer(); };
      list.appendChild(item);
    });
  }

  function showModal(title, desc, icon='💡') {
    document.getElementById('modalTitle').innerText = title;
    document.getElementById('modalDesc').innerHTML = desc;
    document.getElementById('modalIcon').innerText = icon;
    document.getElementById('customModal').classList.add('open');
  }

  function closeModal() {
    playClick();
    document.getElementById('customModal').classList.remove('open');
  }

  // Confetti Canvas
  function triggerConfetti() {
    const canvas = document.getElementById('confettiCanvas');
    const ctx = canvas.getContext('2d');
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;

    const particles = [];
    const colors = ['#0F766E', '#0C4E4B', '#059669', '#DC2626', '#D97706'];

    for (let i = 0; i < 150; i++) {
      particles.push({
        x: Math.random() * canvas.width,
        y: Math.random() * canvas.height - canvas.height,
        size: Math.random() * 10 + 5,
        color: colors[Math.floor(Math.random() * colors.length)],
        speedY: Math.random() * 5 + 3,
        speedX: Math.random() * 2 - 1
      });
    }

    function animate() {
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      particles.forEach(p => {
        p.y += p.speedY;
        p.x += p.speedX;
        ctx.fillStyle = p.color;
        ctx.fillRect(p.x, p.y, p.size, p.size);
      });
      if (particles.some(p => p.y < canvas.height)) {
        requestAnimationFrame(animate);
      }
    }
    animate();
  }

  renderDrawerList();
</script>
</body>
</html>
"""

base_dir = '/Users/nguyenbaouyen/Documents/Chuong-trinh-he-THCS/He-Lop6/H6.01-Thuc-don-vang-cho-tuoi-day-thi'
os.makedirs(os.path.join(base_dir, 'slides'), exist_ok=True)

with open(os.path.join(base_dir, 'generate_slides.py'), 'w', encoding='utf-8') as f:
    f.write(py_code)

print("generate_slides.py updated to 22 slides successfully!")
