-- Crear base de datos base para el gemelo digital
CREATE DATABASE holotwindb;
USE holotwindb;

-- Crear tabla para dispositivos del salón de juegos
CREATE TABLE dispositivos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    tipo VARCHAR(100) NOT NULL,
    descripcion TEXT,
    estado VARCHAR(50) DEFAULT 'activo'
);

-- Crear tabla para el consumo energético los sensores sinteticos
CREATE TABLE consumo_energetico (
    id INT AUTO_INCREMENT PRIMARY KEY,
    dispositivo_id INT,
    fecha DATETIME DEFAULT CURRENT_TIMESTAMP,
    consumo_kWh DECIMAL(10, 2), -- kWh de energía consumida
    FOREIGN KEY (dispositivo_id) REFERENCES dispositivos(id)
);

-- Crear tabla para los sensores sintéticos (los sensores digitales que generarán los datos)
CREATE TABLE sensores (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    tipo_sensor VARCHAR(100),
    descripcion TEXT
);

-- Crear tabla para almacenar las mediciones de los sensores sintéticos
CREATE TABLE mediciones_sensores (
    id INT AUTO_INCREMENT PRIMARY KEY,
    sensor_id INT,
    fecha DATETIME DEFAULT CURRENT_TIMESTAMP,
    valor DECIMAL(10, 2), -- El valor medido por el sensor
    FOREIGN KEY (sensor_id) REFERENCES sensores(id)
);

-- Crear tabla para registrar el consumo de energía por cada escenario simulado
CREATE TABLE simulaciones_consumo (
    id INT AUTO_INCREMENT PRIMARY KEY,
    escenario VARCHAR(255),
    consumo_total DECIMAL(10, 2), -- Consumo total en kWh en ese escenario
    fecha DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Insertar algunos dispositivos en la base de datos
INSERT INTO dispositivos (nombre, tipo, descripcion) VALUES
('PlayStation 5', 'Electrónico', 'Consola de videojuegos de última generación'),
('Aire Acondicionado', 'Electrónico', 'Aire acondicionado para el salón de juegos'),
('Mesa de Hockey', 'Deporte', 'Mesa de hockey para el área de recreo'),
('Billar', 'Deporte', 'Mesa de billar en el salón');

-- Insertar consumo energético de un dispositivo
INSERT INTO consumo_energetico (dispositivo_id, consumo_kWh) VALUES
(1, 0.5), -- PlayStation 5 consume 0.5 kWh
(2, 2.0); -- Aire acondicionado consume 2.0 kWh

-- Insertar sensores sintéticos
INSERT INTO sensores (nombre, tipo_sensor, descripcion) VALUES
('Sensor de Temperatura', 'Térmico', 'Mide la temperatura ambiente en el salón'),
('Sensor de CO2', 'Calidad del Aire', 'Mide el nivel de CO2 en el ambiente');

-- Insertar mediciones de sensores
INSERT INTO mediciones_sensores (sensor_id, valor) VALUES
(1, 22.5), -- Temperatura medida: 22.5°C
(2, 400); -- Nivel de CO2 medido: 400 ppm

-- Insertar una simulación de consumo
INSERT INTO simulaciones_consumo (escenario, consumo_total) VALUES
('Escenario 1: Juego intensivo', 5.5), -- Este escenario simula un consumo total de 5.5 kWh
('Escenario 2: Enfriamiento y recreo', 3.2); -- Este escenario simula 3.2 kWh de consumo

-- Consultar dispositivos y su consumo energético
SELECT d.nombre, SUM(c.consumo_kWh) AS consumo_total
FROM dispositivos d
JOIN consumo_energetico c ON d.id = c.dispositivo_id
GROUP BY d.nombre;

-- Consultar sensores y sus últimas mediciones
SELECT s.nombre, ms.valor, ms.fecha
FROM sensores s
JOIN mediciones_sensores ms ON s.id = ms.sensor_id
ORDER BY ms.fecha DESC
LIMIT 5;

-- Consultar simulaciones de consumo
SELECT * FROM simulaciones_consumo;
