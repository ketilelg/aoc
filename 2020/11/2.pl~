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
	    elsif (($seats[$y][$x] eq "#") && ($neigh >= 4)) { $newseats[$y][$x] = "L"; $change++;}
	    else { $newseats[$y][$x] = $seats[$y][$x];}
	    if ($newseats[$y][$x] eq "#") { $nseats++; }
	}
    }
#    print "seats: \n";
#    printseats( @seats );
    @seats = @{ dclone(\@newseats)};
    print "nseats: \n";
    printseats( @seats );
    print "occ: $nseats $change\n\n";

}



sub numocc
{
    my $xp=$_[0];
    my $yp=$_[1];
    my $num=0;
    for my $x  (($xp < 1 ? 0 : ($xp - 1))..(($xp > ($width-1) ? $width : ($xp + 1)))) {
	for my $y  (($yp < 1 ? 0 : ($yp - 1))..(($yp > ($height-1) ? $height : ($yp + 1)))) {
	    if (!(($x==$xp)&&($y==$yp))&&($seats[$y][$x] eq "#")) { $num++;}
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

