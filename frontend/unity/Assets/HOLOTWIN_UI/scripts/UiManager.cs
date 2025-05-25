using UnityEngine;
using UnityEngine.UI;
using TMPro;
using UnityEngine.Networking;
using System.Collections;

public class UiManager : MonoBehaviour
{
    public TMP_Text txtConsumoActual;
    public TMP_Text txtRecomendacion;
    public Button btnObtenerRecomendacion;
    public Button btnExportarPDF;

    string apiURL = "http://localhost:8000/api/recomendaciones";

    void Start()
    {
        btnObtenerRecomendacion.onClick.AddListener(() => StartCoroutine(EnviarRecomendacion(false)));
        btnExportarPDF.onClick.AddListener(() => StartCoroutine(EnviarRecomendacion(true)));
    }

    IEnumerator EnviarRecomendacion(bool exportarPDF)
    {
        string endpoint = exportarPDF ? "/recomendar/pdf" : "/recomendar";
        string sala = "Sala de Juegos";
        float consumo = Random.Range(10f, 30f);
        string[] dispositivos = new string[] { "TV", "PS5", "AC", "Luz" };

        string json = JsonUtility.ToJson(new DatosEnvio(sala, consumo, dispositivos));

        UnityWebRequest request = new UnityWebRequest(apiURL + endpoint, "POST");
        byte[] bodyRaw = System.Text.Encoding.UTF8.GetBytes(json);
        request.uploadHandler = new UploadHandlerRaw(bodyRaw);
        request.downloadHandler = new DownloadHandlerBuffer();
        request.SetRequestHeader("Content-Type", "application/json");

        yield return request.SendWebRequest();

        if (request.result == UnityWebRequest.Result.Success)
        {
            if (!exportarPDF)
            {
                RespuestaIA respuesta = JsonUtility.FromJson<RespuestaIA>(request.downloadHandler.text);
                txtConsumoActual.text = $"Consumo estimado: {consumo:F1} kWh";
                txtRecomendacion.text = "💡 " + respuesta.recomendacion;
            }
            else
            {
                txtRecomendacion.text = "📄 Recomendación exportada como PDF correctamente.";
            }
        }
        else
        {
            txtRecomendacion.text = "⚠️ Error al conectar con el backend.";
        }
    }

    [System.Serializable]
    class DatosEnvio
    {
        public string sala;
        public float consumo;
        public string[] dispositivos;

        public DatosEnvio(string sala, float consumo, string[] dispositivos)
        {
            this.sala = sala;
            this.consumo = consumo;
            this.dispositivos = dispositivos;
        }
    }

    [System.Serializable]
    class RespuestaIA
    {
        public string recomendacion;
    }
}
