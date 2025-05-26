using UnityEngine;
using UnityEngine.UI;
using TMPro;
using UnityEngine.Networking;
using System.Collections;
using System.Collections.Generic;

public class UiManager : MonoBehaviour
{
    public TMP_InputField inputConsumo;
    public TMP_Text txtRecomendacion;
    public Button btnObtenerRecomendacion;
    public Button btnExportarPDF;
    public Button btnDescargarPDF;
    public List<Toggle> togglesDispositivos;

    private string apiUrl = "http://localhost:8000/api/recomendaciones";
    private string rutaPDF;

    void Start()
    {
        btnObtenerRecomendacion.onClick.AddListener(() => StartCoroutine(EnviarRecomendacion(false)));
        btnExportarPDF.onClick.AddListener(() => StartCoroutine(EnviarRecomendacion(true)));
        btnDescargarPDF.onClick.AddListener(() => Application.OpenURL(rutaPDF));
        btnDescargarPDF.gameObject.SetActive(false); // Oculto al inicio
    }

    IEnumerator EnviarRecomendacion(bool exportarPDF)
    {
        if (string.IsNullOrEmpty(inputConsumo.text))
        {
            txtRecomendacion.text = "⚠️ Ingresa un valor de consumo.";
            yield break;
        }

        if (!float.TryParse(inputConsumo.text, out float consumo))
        {
            txtRecomendacion.text = "⚠️ El valor debe ser numérico.";
            yield break;
        }

        List<string> dispositivosSeleccionados = new List<string>();
        foreach (Toggle toggle in togglesDispositivos)
        {
            if (toggle.isOn)
            {
                TMP_Text texto = toggle.GetComponentInChildren<TMP_Text>();
                if (texto != null)
                    dispositivosSeleccionados.Add(texto.text);
            }
        }

        if (dispositivosSeleccionados.Count == 0)
        {
            txtRecomendacion.text = "⚠️ Selecciona al menos un dispositivo.";
            yield break;
        }

        string endpoint = exportarPDF ? "/recomendar/pdf" : "/recomendar";

        DatosEnvio data = new DatosEnvio
        {
            sala = "Sala de Juegos",
            consumo = consumo,
            dispositivos = dispositivosSeleccionados
        };

        string json = JsonUtility.ToJson(data);

        UnityWebRequest request = new UnityWebRequest(apiUrl + endpoint, "POST");
        byte[] bodyRaw = System.Text.Encoding.UTF8.GetBytes(json);
        request.uploadHandler = new UploadHandlerRaw(bodyRaw);
        request.downloadHandler = new DownloadHandlerBuffer();
        request.SetRequestHeader("Content-Type", "application/json");

        // 🔐 Si el usuario está autenticado, incluye el token JWT
        if (!string.IsNullOrEmpty(LoginManager.jwtToken))
        {
            request.SetRequestHeader("Authorization", "Bearer " + LoginManager.jwtToken);
        }

        yield return request.SendWebRequest();

        if (request.result == UnityWebRequest.Result.Success)
        {
            if (!exportarPDF)
            {
                RespuestaIA respuesta = JsonUtility.FromJson<RespuestaIA>(request.downloadHandler.text);
                txtRecomendacion.text = $"💡 Recomendación: {respuesta.recomendacion}";
                btnDescargarPDF.gameObject.SetActive(false);
            }
            else
            {
                RespuestaPDF respuesta = JsonUtility.FromJson<RespuestaPDF>(request.downloadHandler.text);
                txtRecomendacion.text = "📄 Reporte generado correctamente.";
                rutaPDF = "http://localhost:8000" + respuesta.ruta_pdf;
                btnDescargarPDF.gameObject.SetActive(true);
            }
        }
        else
        {
            txtRecomendacion.text = "❌ Error al conectar con el backend.";
        }
    }

    [System.Serializable]
    public class DatosEnvio
    {
        public string sala;
        public float consumo;
        public List<string> dispositivos;
    }

    [System.Serializable]
    public class RespuestaIA
    {
        public string recomendacion;
    }

    [System.Serializable]
    public class RespuestaPDF
    {
        public string msg;
        public string recomendacion;
        public string ruta_pdf;
    }
}