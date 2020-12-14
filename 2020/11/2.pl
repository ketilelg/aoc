#!/usr/bin/perl

use Storable qw(dclone);

my @seats;
my @newseats;
my $row=0;
my $height;
while (<>)
{
    chomp;
    $seats[$row] = [ split // ];

    $width=length;
    $row++;
}

my $height=$row--;



print "l: $height w: $width\n";
my $change=1;
while($change){

    $change=0;
    my $nseats=0;
    for my  $y  (0..$height) {
    

	for my $x (0..$width)  {

	    #	    print "\nw: $x $y\n\n";
	    my $neigh=numocc($x,$y);
#	    print "w: $x $y $seats[$y][$x] $neigh\n\n";
	    if (($seats[$y][$x] eq "L") && ($neigh == 0)) { $newseats[$y][$x] = "#"; $change++;}
	    elsif (($seats[$y][$x] eq "#") && ($neigh >= 5)) { $newseats[$y][$x] = "L"; $change++;}
	    else { $newseats[$y][$x] = $seats[$y][$x];}
	    if ($newseats[$y][$x] eq "#") { $nseats++; }
	}
    }
#    print "seats: \n";
#    printseats( @seats );
    @seats = @{ dclone(\@newseats)};
    print "nseats: \n";
#    printseats( @seats );
    print "occ: $nseats $change\n\n";

}



sub numocc
{
    my $xp=$_[0];
    my $yp=$_[1];
    my $num=0;
    for my $x (-1..1)
    {
	for my $y (-1..1)
	{
	    if(($x!=0)||($y!=0))
	    {
		
	    #x,y er retningsvektor..

		for my $dist (1..100)

		{
		    my $tx=$xp+($dist*$x);
		    my $ty=$yp+($dist*$y);
		    if(($tx < 0) || ($ty < 0) || ($tx > $width-1) || ($ty > $height -1)) { last; }
		    if($seats[$ty][$tx] eq "#") {$num++; last;}
		    if($seats[$ty][$tx] eq "L") {last;}
		}
	    }
		
#	    print "nf: $x $y $num $seats[$y][$x]\n";
	}
    }
    return $num;

}

sub printseats
{
    for my  $y (0..$height) {
	for my $x (0..$width) {
	    print $_[$y][$x];
	}
	print "\n";
    }
}

