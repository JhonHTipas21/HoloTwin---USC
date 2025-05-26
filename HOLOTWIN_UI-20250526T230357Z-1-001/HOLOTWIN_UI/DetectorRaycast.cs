using UnityEngine;
using UnityEngine.InputSystem;
using TMPro;

public class DetectorRaycast : MonoBehaviour
{
    [SerializeField] private LayerMask interactableLayer;
    public Camera mainCamera;
    public UI3DOverlay overlayUI;

    void Update()
    {
        // Detectar clic con el nuevo Input System
        if (Mouse.current.leftButton.wasPressedThisFrame)
        {
            Ray ray = mainCamera.ScreenPointToRay(Mouse.current.position.ReadValue());
            RaycastHit hit;

            if (Physics.Raycast(ray, out hit, Mathf.Infinity, interactableLayer))
            {
                GameObject objetoSeleccionado = hit.collider.gameObject;
                Debug.Log("Clic sobre: " + objetoSeleccionado.name);

                // Verifica si el objeto tiene el componente ObjetoInteractivo
                ObjetoInteractivo info = objetoSeleccionado.GetComponent<ObjetoInteractivo>();
                if (info != null && overlayUI != null)
                {
                    overlayUI.MostrarInfo(info.nombre, info.estado);
                }

                // (Opcional) cambiar color del objeto clicado
                Renderer renderer = objetoSeleccionado.GetComponent<Renderer>();
                if (renderer != null)
                {
                    renderer.material.color = Color.yellow;
                }
            }
        }

        // Cierra el panel si presiona ESC
        if (Keyboard.current.escapeKey.wasPressedThisFrame && overlayUI != null)
        {
            overlayUI.OcultarInfo();
        }
    }
}
