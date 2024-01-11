-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Waktu pembuatan: 11 Jan 2024 pada 17.42
-- Versi server: 10.4.28-MariaDB
-- Versi PHP: 8.0.28

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `bmi`
--

-- --------------------------------------------------------

--
-- Struktur dari tabel `cewe`
--

CREATE TABLE `cewe` (
  `id` int(11) NOT NULL,
  `jk` varchar(1) DEFAULT NULL,
  `berat` double DEFAULT NULL,
  `tinggi` double DEFAULT NULL,
  `bmi` double DEFAULT NULL,
  `kategori` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `cewe`
--

INSERT INTO `cewe` (`id`, `jk`, `berat`, `tinggi`, `bmi`, `kategori`) VALUES
(2, 'p', 83, 160, 32.4, 'Obesitas');

-- --------------------------------------------------------

--
-- Struktur dari tabel `cowo`
--

CREATE TABLE `cowo` (
  `id` int(11) NOT NULL,
  `jk` varchar(1) NOT NULL,
  `berat` double NOT NULL,
  `tinggi` double NOT NULL,
  `bmi` double NOT NULL,
  `kategori` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `cowo`
--

INSERT INTO `cowo` (`id`, `jk`, `berat`, `tinggi`, `bmi`, `kategori`) VALUES
(10, 'l', 76, 183, 22, 'Ideal'),
(11, 'l', 83, 183, 24, 'Ideal'),
(12, 'l', 84, 183, 25.1, 'Gemuk');

--
-- Indexes for dumped tables
--

--
-- Indeks untuk tabel `cewe`
--
ALTER TABLE `cewe`
  ADD PRIMARY KEY (`id`);

--
-- Indeks untuk tabel `cowo`
--
ALTER TABLE `cowo`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT untuk tabel yang dibuang
--

--
-- AUTO_INCREMENT untuk tabel `cewe`
--
ALTER TABLE `cewe`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT untuk tabel `cowo`
--
ALTER TABLE `cowo`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
