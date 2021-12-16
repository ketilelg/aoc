#!/usr/bin/perl


my $in=<>;
chomp $in;

my $bs;
for my $c (split //, $in)
{
    $bs .= sprintf "%.4b", "0x$c";
}

print "bs: -$bs-\n";

sub parse
    #tar streng som pint
{
    my $pos=0;
    my $bs=$_[0];
    my $ver=substr $bs,$pos,3;
    $pos+=3;
    my $v=oct("0b$ver");
    print "$v\n";
    $tid=substr $bs,$pos,3;
    $pos+=3;
    my $t=oct("0b$tid");
    print "tid:$tid $t\n";
    if ($t == 4)
    {
	my $n; #number string
	my $cont=1;
	while($cont)
	{
	    my $sstr=substr $bs,$pos,5;
	    if (substr($sstr,0,1) eq "0")
	    {
		$cont = 0;
	    }
	    $n.=substr($sstr,1,4);
	    print "sstr: $sstr\n";
	    $pos+=5;
	}
	$xv=oct("0b$n");
	print "x: $xv\n";

    }
    else #er operator
    {
	$lti=substr($bs,$pos,1);
	$pos++;
	if ($lti eq "0")
	{
	    $tlen=substr($bs,$pos,15);
	    $pos+=15;
	    my $tt=oct("0b$tlen");
	    print "tlen: $tt\n";
	}
	else
	{
	    $npack=substr($bs,$pos,11);
	    $pos+=11;
	    my $tt=oct("0b$npack");
	    print "npack: $tt\n";
	}
    }
}

parse($bs);
