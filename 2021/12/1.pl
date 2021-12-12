#!/usr/bin/perl

my @in1;
my @in2;
my $n=1;

@in1[0]="sss";
@in2[0]="start";
# @in1[1]="start";
# @in2[1]="sss";

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

@in1[$n]="end";
@in2[$n]="eee";
$n++;
@in1[$n]="eee";
@in2[$n]="end";

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
    $rd++;
    $visits{$w}++;
    print "rd: $rd w: $w $visits{$w} s:$s\n";
    if (($w ne "end") && (isup($w) || ($visits{$w} < 2)))
    {
	for $i (0..$n)
	{
#	    print "fl - $i $in1[$i] $in2[$i]\n";
	    if ($in1[$i] eq $w)
	    {
#		print "eq $i $in1[$i] $in2[$i] $w \n";
		rec($in2[$i],$s . "," . "$w",$rd);
	    }
	}
    }
    if ($w eq "end")
    {
	$r++;
	print "END: $r $s,end\n";
    }
    print "al: $w $visits{$w}\n";
    $visits{$w}--;
}

print "n: $n\n";
rec("sss","->",0);

