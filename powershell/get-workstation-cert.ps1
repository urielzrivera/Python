# Usage: .\Get-RemoteCert.ps1 -HostName "google.com" -Port 443

param (
    [Parameter(Mandatory = $true)]
    [string]$HostName,   # e.g., "example.com" or IP address
 
    [Parameter(Mandatory = $true)]
    [int]$Port           # e.g., 443
)
 
try {
    # Connect to the remote host and port
    $tcpClient = New-Object System.Net.Sockets.TcpClient
    $tcpClient.Connect($HostName, $Port)
 
    # Create SSL stream
    $sslStream = New-Object System.Net.Security.SslStream(
        $tcpClient.GetStream(),
        $false,
        { $true } # Accept all certificates (no validation)
    )
 
    # Initiate SSL handshake
    $sslStream.AuthenticateAsClient($HostName)
 
    # Retrieve the remote certificate
    $cert = New-Object System.Security.Cryptography.X509Certificates.X509Certificate2($sslStream.RemoteCertificate)
 
    # Output certificate details
    [PSCustomObject]@{
        Subject        = $cert.Subject
        Issuer         = $cert.Issuer
        NotBefore      = $cert.NotBefore
        NotAfter       = $cert.NotAfter
        Thumbprint     = $cert.Thumbprint
        SerialNumber   = $cert.SerialNumber
        SignatureAlgo  = $cert.SignatureAlgorithm.FriendlyName
        DNSNames       = ($cert.Extensions |
                          Where-Object { $_.Oid.FriendlyName -eq "Subject Alternative Name" } |
                          ForEach-Object { $_.Format($true) })
    }
}
catch {
    Write-Error "Failed to retrieve certificate from $HostName : $Port - $_"
}
finally {
    # Clean up resources
    if ($sslStream) { $sslStream.Dispose() }
    if ($tcpClient) { $tcpClient.Close() }
}
