exec { 'fix':
    command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
}
