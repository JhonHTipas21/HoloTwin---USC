using System.Windows;
using LiveChartsCore;
using LiveChartsCore.SkiaSharpView;
using LiveChartsCore.SkiaSharpView.Painting;
using SkiaSharp;

namespace HOLOTWIN_USC.frontend
{
    public partial class MainWindow : Window
    {
        public MainWindow()
        {
            InitializeComponent(); // Este método es generado automáticamente por el sistema, no es necesario implementarlo.
            ConfigurarGraficos();
        }

        private void ConfigurarGraficos()
        {
            // Configuración del primer gráfico
            Chart1.Series = new ISeries[]
            {
                new LineSeries<double>
                {
                    Values = new double[] { 10, 12, 8, 15, 18, 14, 10 },
                    Fill = null,
                    Stroke = new SolidColorPaint(SKColors.Green) { StrokeThickness = 2 }
                }
            };

            // Configuración del segundo gráfico
            Chart2.Series = new ISeries[]
            {
                new LineSeries<double>
                {
                    Values = new double[] { 5, 9, 7, 12, 15, 13, 11 },
                    Fill = null,
                    Stroke = new SolidColorPaint(SKColors.Blue) { StrokeThickness = 2 }
                }
            };
        }

        private void Iniciar_Click(object sender, RoutedEventArgs e)
        {
            MessageBox.Show("Iniciando simulación...");
        }

        private void VerResultados_Click(object sender, RoutedEventArgs e)
        {
            MessageBox.Show("Mostrando resultados...");
        }

        private void Detener_Click(object sender, RoutedEventArgs e)
        {
            MessageBox.Show("Simulación detenida.");
        }
    }
}
