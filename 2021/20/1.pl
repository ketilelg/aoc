#!/usr/bin/perl

my $ls=<>;
my @lut=split //,$ls;
my $ls=<>; #skip line
my $line=1;
my @map;
while(<>)
{
    chomp;
    $w=length;
    my @lc=split//;
    for my $c (0..$#lc)
    {
        $map[$line][$c+1]=$lc[$c];
    }

    $line++;
    
}

my $space=".";


sub printmap
{
    print "pm: $w, $line space:$space\n";
    for my $y (0..$line)
    {
	for my $x (0..$w+1)
	{
	    print $map[$y][$x];
	}
	print "\n";
    }
}    

my $nlit;

sub generation
{
    my @nmap;
    $nlit=0;
    for my $y(0..$line+1)
    {
	for my $x(0..$w+2)
	{
	    my $pv=0;	
	    for my $by($y-1..$y+1)
	    {
		for my $bx($x-1..$x+1)
		{
		    $pv*=2;
		    if (($by>0) && ($bx>0) && ($by<$line+1) && ($bx<$w+2))
		    { #innenfor $map
			if ($map[$by-1][$bx-1] eq "#")
			{
			    $pv++;
			}
		    }
		    else
		    { #utenfor, anse at vi må se på "outer space"
			if($space eq "#")
			{
			    $pv++;
			}
		    }
		}

	    }
	    $nmap[$y][$x]=$lut[$pv];
	    if($nmap[$y][$x] eq "#")
	    {
		$nlit++;
	    }
	}
    }
    $w+=2;
    $line+=2;
    @map=@nmap;
    if($space eq "#") #outer space er enten alle eller ingen..:
    { #alle på
	$space=$lut[511];
    }
    else
    { #alle mørke
	$space=$lut[0];
    }
}

generation;
generation;

print "part1: $nlit\n";

for my $i (0..47)
{
    generation;
}
print "part2: $nlit\n";
