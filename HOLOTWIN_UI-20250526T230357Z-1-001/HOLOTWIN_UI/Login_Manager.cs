using UnityEngine;
using UnityEngine.UI;
using TMPro;
using UnityEngine.Networking;
using System.Collections;

public class LoginManager : MonoBehaviour
{
    public TMP_InputField inputEmail;
    public TMP_InputField inputPassword;
    public TMP_Text txtLoginError;
    public Button btnLogin;
    public GameObject panelLogin;
    public GameObject panelDashboard;
    public Button btnCerrarSesion;

    public static string jwtToken = "";

    void Start()
    {
        btnLogin.onClick.AddListener(() => StartCoroutine(LoginUsuario()));
        txtLoginError.text = "";
        btnCerrarSesion.onClick.AddListener(CerrarSesion);
    }

    IEnumerator LoginUsuario()
    {
        if (string.IsNullOrEmpty(inputEmail.text) || string.IsNullOrEmpty(inputPassword.text))
        {
            txtLoginError.text = "⚠️ Ingresa email y contraseña.";
            yield break;
        }

        var loginData = new LoginData
        {
            email = inputEmail.text,
            password = inputPassword.text
        };

        string json = JsonUtility.ToJson(loginData);

        UnityWebRequest request = new UnityWebRequest("http://localhost:8000/login", "POST");
        byte[] bodyRaw = System.Text.Encoding.UTF8.GetBytes(json);
        request.uploadHandler = new UploadHandlerRaw(bodyRaw);
        request.downloadHandler = new DownloadHandlerBuffer();
        request.SetRequestHeader("Content-Type", "application/json");

        yield return request.SendWebRequest();

        if (request.result == UnityWebRequest.Result.Success)
        {
            LoginResponse response = JsonUtility.FromJson<LoginResponse>(request.downloadHandler.text);
            jwtToken = response.access_token;

            // Ocultar login, mostrar dashboard
            panelLogin.SetActive(false);
            panelDashboard.SetActive(true);
        }
        else
        {
            txtLoginError.text = "❌ Login inválido. Verifica tus datos.";
        }
    }

    [System.Serializable]
    public class LoginData
    {
        public string email;
        public string password;
    }

    [System.Serializable]
    public class LoginResponse
    {
        public string access_token;
        public string token_type;
    }
    void CerrarSesion()
    {
        jwtToken = "";
        panelDashboard.SetActive(false);
        panelLogin.SetActive(true);
    }
}