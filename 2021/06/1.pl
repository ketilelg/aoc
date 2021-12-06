#!/usr/bin/perl

@fishinput=split(",",<>);

my @nf=(0,0,0,0,0,0,0,0,0);

foreach $f (@fishinput)
{
    $nf[$f]++;
}

my $n;

for my $d (0..255)
{

    my @of = @nf;
    $nf[8]=$of[0];
    $nf[7]=$of[8];
    $nf[6]=$of[7]+$of[0];
    $nf[5]=$of[6];
    $nf[4]=$of[5];
    $nf[3]=$of[4];
    $nf[2]=$of[3];
    $nf[1]=$of[2];
    $nf[0]=$of[1];
    $n=0;
    for my $i (0..8)
    {
	$n+=$nf[$i];
    }
    print "dag: $d antall: $n\n";
}




