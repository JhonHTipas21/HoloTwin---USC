using UnityEngine;

public class ObjetoInteractivo : MonoBehaviour
{
    public string nombreDispositivo;
    public float consumoSimulado;
    public string nombre;
    public string estado;

    public void MostrarInformacion()
    {
        Debug.Log($"👉 Dispositivo: {nombreDispositivo} — Consumo: {consumoSimulado} kWh");
        UI3DOverlay.Instance.MostrarPanel(nombreDispositivo, consumoSimulado);
    }
}