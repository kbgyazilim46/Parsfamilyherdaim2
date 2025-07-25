from flask import Flask

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <title>HAYALET FAMİLY HAKKINDA</title>
    <style>
        body {{ font-family: Arial, sans-serif; background: #f4f4f4; padding: 20px; }}
        nav a {{ margin: 10px; text-decoration: none; color: #333; font-weight: bold; }}
        .container {{ max-width: 800px; margin: auto; background: white; padding: 20px; border-radius: 8px; box-shadow: 0 0 10px rgba(0,0,0,0.1); }}
        h1 {{ color: #444; }}
    </style>
</head>
<body>
    <nav>
        <a href="/">Hakkında</a>
        <a href="/iletisim">İletişim</a>
    </nav>
    <div class="container">
        %%CONTENT%%
    </div>
</body>
</html>
"""
<h1>HAYALET FAMILY</h1>
    <p>Gücümüz Birliğimizden Gelir</p>
  </header>

  <section>
    <h2>Hakkımızda</h2>
    <p>
      Hayalet Family, sanal alemde ismini duyurmuş güçlü bir gruptur. Tag’ımızı taşıyan her birey bu ailenin bir parçasıdır.
    </p>
    <ul>
      <li><strong>Baş Kurucu:</strong> Kimsebaşgözedemezdir</li>
      <li><strong>Baş Leader:</strong> Leaxs Santo</li>
      <li><strong>1. Leader:</strong> Versace</li>
    </ul>
  </section>

  <section>
    <h2>İletişim & Instagram Hesaplarımız</h2>
    <ul>
      <li>📌 <a href="https://instagram.com/hayaletfamily.resmihesap" target="_blank">@hayaletfamily.resmihesap</a></li>
      <li>👑 <a href="https://instagram.com/_hayalet.bas.krc.kimsebasgoz_" target="_blank">@_hayalet.bas.krc.kimsebasgoz_</a></li>
      <li>🧠 <a href="https://instagram.com/hayalet.leaxs" target="_blank">@hayalet.leaxs</a></li>
      <li>⚔️ <a href="https://instagram.com/hayalet.versace" target="_blank">@hayalet.versace</a></li>
    </ul>
  </section>

  <footer>
    ©2025 Pars Family. Tüm hakları saklıdır.
