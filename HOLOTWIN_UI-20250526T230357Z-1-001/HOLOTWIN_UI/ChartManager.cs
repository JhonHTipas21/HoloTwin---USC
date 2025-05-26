using UnityEngine;
using UnityEngine.UI;
using TMPro;
using System.Collections.Generic;

public class ChartManager : MonoBehaviour
{
    public TMP_Dropdown dropdownRango;
    public GameObject barraPrefab; // Prefab simple de barra (una Image)
    public Transform contenedorBarras; // Donde se instancian

    int cantidadBarras = 7;

    void Start()
    {
        dropdownRango.onValueChanged.AddListener(ActualizarGrafico);
        ActualizarGrafico(0); // Inicializa
    }

    void ActualizarGrafico(int opcion)
    {
        foreach (Transform child in contenedorBarras)
        {
            Destroy(child.gameObject);
        }

        switch (opcion)
        {
            case 0: cantidadBarras = 1; break;   // Hoy
            case 1: cantidadBarras = 7; break;   // Semana
            case 2: cantidadBarras = 30; break;  // Mes
        }

        for (int i = 0; i < cantidadBarras; i++)
        {
            GameObject barra = Instantiate(barraPrefab, contenedorBarras);
            RectTransform rt = barra.GetComponent<RectTransform>();
            float altura = Random.Range(20f, 150f);
            rt.sizeDelta = new Vector2(30, altura);

            TextMeshProUGUI etiqueta = barra.GetComponentInChildren<TextMeshProUGUI>();
            if (etiqueta != null)
                etiqueta.text = $"{Mathf.RoundToInt(altura)} kWh";
        }
    }
}