<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>Telegram Login</title>
  <style>
    body {
      margin: 0;
      padding: 0;
      font-family: 'Segoe UI', sans-serif;
      background-color: #e0ebf5;
      display: flex;
      justify-content: center;
      align-items: center;
      height: 100vh;
    }

    .login-container {
      background-color: white;
      padding: 40px;
      border-radius: 12px;
      box-shadow: 0 8px 20px rgba(0,0,0,0.15);
      max-width: 360px;
      width: 100%;
      text-align: center;
    }

    .login-container h2 {
      margin-bottom: 10px;
      color: #0088cc;
    }

    .login-container p {
      color: #666;
      font-size: 14px;
      margin-bottom: 20px;
    }

    input {
      width: 100%;
      padding: 12px;
      margin: 10px 0;
      border: 1px solid #ccc;
      border-radius: 6px;
      font-size: 16px;
    }

    button {
      background-color: #0088cc;
      color: white;
      padding: 12px;
      border: none;
      border-radius: 6px;
      font-size: 16px;
      cursor: pointer;
      width: 100%;
      margin-top: 10px;
    }

    button:hover {
      background-color: #0077b3;
    }

    .footer {
      margin-top: 20px;
      font-size: 12px;
      color: #999;
    }
  </style>
</head>
<body>

  <div class="login-container">
    <h2>Telegram Login</h2>
    <p>Log in with your phone number</p>

    <form onsubmit="event.preventDefault(); alert('Logged in (dummy)!');">
      <input type="text" placeholder="+1 123 456 7890" required />
      <input type="password" placeholder="Code or Password" required />
      <button type="submit">Next</button>
    </form>

    <div class="footer">
      Not registered? Use Telegram app to sign up.
    </div>
  </div>

</body>
</html>