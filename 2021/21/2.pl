#!/usr/bin/perl

my %dice = ( 3=>1,
	     4=>3,
	     5=>6,
	     6=>7,
	     7=>6,
	     8=>3,
	     9=>1 ); # value, number of reps

my @wins; #wins pr spiller
my $nrolls=0;
my $maxscore=0;

# while() #ikke alle tenkelige er avgjort
sub play
    # rekursiv spilling. tar input: spillerno, posp1, posp2, scorep1, scorep2, numuni, rdept (rdept for debugformål)
{
    my $np;
    my $p=$_[0];
    if ($p)
    {
	$np=0;
    }
    else
    {
	$np=1;
    }
    
    my @pos;
    $pos[0]=$_[1];
    $pos[1]=$_[2];
    my @score;
    $score[0]=$_[3];
    $score[1]=$_[4];
    my $numuni=$_[5];
    my $rdep=$_[6]+1;


    for my $diev (keys %dice)
    {
	my @nscore=@score;
	my @npos=@pos;
	# $dice{$diev} inneholder antall univers som har denne varianten
	# $diev er verdien av 3-kastet.

	my $ndice = $dice{$diev}; #ndice er da antall.
	
	$npos[$p] =  (($pos[$p] + $diev -1) % 10) + 1;
	$nscore[$p] = $score[$p] + $npos[$p];

	if ($nscore[$p] > 20)
	{
	    $wins[$p]+=$numuni*$ndice;
	}
	else
	{
	    play($np,$npos[0],$npos[1],$nscore[0],$nscore[1],$numuni*$ndice,$rdep);
	}
    }
}


play(0,1,2,0,0,1,0);

print "wins: \n$wins[0] \n$wins[1] \n";
