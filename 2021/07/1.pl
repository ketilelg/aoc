#!/usr/bin/perl

@crabs=split(",", <>);

print "@crabs";

my $sum;
my $min=1000000;
my $max=0;
my $shortest=100000000;
foreach my $c (@crabs)
{
    $sum+=$c;
    if ($min > $c) {$min=$c;}
    if ($max < $c) {$max=$c;}

    my $sd=0;
    foreach my $cc (@crabs)
    {
	#finn sumavstand
	$sd+=abs($cc-$c);
    }
    print "c: $c sd: $sd\n";
    if ($shortest>$sd) {$shortest=$sd;}
}

$avg= $sum/($#crabs+1);
print "sum: $sum, avg: $avg $min $max shortest: $shortest\n";
