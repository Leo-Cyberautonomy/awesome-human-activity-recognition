# Validates Markdown links using lychee (https://github.com/lycheeverse/lychee).
# Requires Rust toolchain or prebuilt binaries; instructs installation if missing.

param(
    [switch]$Install
)

$ErrorActionPreference = "Stop"

function Ensure-Lychee {
    $lychee = Get-Command lychee -ErrorAction SilentlyContinue
    if (-not $lychee) {
        if (-not $Install) {
            Write-Host "lychee CLI not found. Rerun with -Install to download a prebuilt binary." -ForegroundColor Yellow
            exit 1
        }

        $tmpDir = Join-Path $env:TEMP "lychee-download"
        if (-not (Test-Path $tmpDir)) {
            New-Item -ItemType Directory -Path $tmpDir | Out-Null
        }

        Write-Host "Downloading lychee v0.15.1..." -ForegroundColor Cyan
        $zipPath = Join-Path $tmpDir "lychee.zip"
        $uri = "https://github.com/lycheeverse/lychee/releases/download/v0.15.1/lychee-v0.15.1-x86_64-pc-windows-msvc.zip"
        Invoke-WebRequest -Uri $uri -OutFile $zipPath

        Write-Host "Extracting lychee..." -ForegroundColor Cyan
        Expand-Archive -Path $zipPath -DestinationPath $tmpDir -Force
        $binPath = Join-Path $tmpDir "lychee.exe"

        $target = Join-Path $PSScriptRoot "bin"
        if (-not (Test-Path $target)) {
            New-Item -ItemType Directory -Path $target | Out-Null
        }

        Copy-Item -Path $binPath -Destination (Join-Path $target "lychee.exe") -Force
        $env:PATH = "$target;$env:PATH"
        Write-Host "lychee installed to $target" -ForegroundColor Green
    }
}

Ensure-Lychee

$argsList = @(
    "--verbose",
    "--no-progress",
    "--accept", "200,203,206,302,999",
    "--max-concurrency", "8",
    (Join-Path (Get-Location) "**/*.md")
)

Write-Host "Running lychee..." -ForegroundColor Cyan
lychee @argsList
