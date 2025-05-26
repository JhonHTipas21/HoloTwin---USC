using UnityEngine;
using TMPro;

public class UI3DOverlay : MonoBehaviour
{
    public GameObject panelInfo;
    public TMP_Text nombreTxt;
    public TMP_Text estadoTxt;


    public void MostrarInfo(string nombre, string estado)
    {
        nombreTxt.text = nombre;
        estadoTxt.text = estado;
        panelInfo.SetActive(true);
    }

    public void OcultarInfo()
    {
        panelInfo.SetActive(false);
    }
}
