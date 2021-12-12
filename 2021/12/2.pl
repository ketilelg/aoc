#!/usr/bin/perl

my @in1;
my @in2;
my $n=0;

while (<>)
{
    chomp;
    /(\w+)-(\w+)/;
    @in1[$n]=$1;
    @in2[$n]=$2;
    $n++;
    @in1[$n]=$2;
    @in2[$n]=$1;
    $n++
}

$n--;

#vi har to tabeller, <n> identifiserer linjestykke. vi har begge retninger, for å slippe
#å se rundt.. 

sub isup
    #retur true om parameter er upcase
{
    my $tt=$_[0];
        return ($tt =~ /[[:upper:]]+/);
}

my %visits;
my $r=0;



sub rec
    # tar startpos som input, kjør rekursivt til vi kommer til end. 
{
    my $w=$_[0];
    my $s=$_[1];
    my $rd=$_[2]; #recursion depth;
    my $dvisit=$_[3]; # rom som tåler dobbeltbesøk
    $rd++;
    $visits{$w}++;

    if ( ($visits{$w} == 2) && ($w ne "start") && ($w ne "end") && !isup($w) && ($dvisit eq " ")  )
    {
	$dvisit=$w;
    }
    
    if (($w ne "end") && (isup($w) || ($visits{$w} < 2) || (($visits{$w} == 2) && $dvisit eq $w)))
    {
	for $i (0..$n)
	{
	    if ($in1[$i] eq $w)
	    {
		rec($in2[$i],$s . "," . "$w",$rd,$dvisit);
	    }
	}
    }
    if ($w eq "end")
    {
	$r++;
#	print "END: $r $s,end\n";
    }
    $visits{$w}--;
}

rec("start","->",0," ");

print "del2: $r\n";
