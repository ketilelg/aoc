#!/usr/bin/perl


my $in=<>;
chomp $in;

my $bs;
for my $c (split //, $in)
{
    $bs .= sprintf "%.4b", "0x$c";
}

my $vsum=0;

sub parse
    #tar streng som input, returnerer verdi, og antall bits spist? (bits, verdi)
{
    my $pos=0;
    my $bs=$_[0];

#    print "p: $bs\n";
    my $ver=substr $bs,$pos,3;
    $pos+=3;
    my $v=oct("0b$ver");
#    print "ver $v\n";
    $vsum+=$v;
    $tid=substr $bs,$pos,3;
    $pos+=3;
    my $t=oct("0b$tid");
#    print "tid: $t\n";
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
#	    print "sstr: $sstr\n";
	    $pos+=5;
	}
	$xv=oct("0b$n");
#	print "x: $xv\n";
	return $pos,$xv;
    }
    else #er operator
    {
	my $val=0;
	$lti=substr($bs,$pos,1);
	$pos++;
	if ($lti eq "0")
	{ #number of bits
	    $tlen=substr($bs,$pos,15);
	    $pos+=15;
	    my $tt=oct("0b$tlen");
#	    print "tlen: $tt\n";
	    my $ll,$vv;
	    ($ll,$vv)=parse(substr($bs,$pos));
	    $val=$vv;
	    $pos+=$ll;
	    $tt-=$ll;
	    while ($tt > 0)
	    {
		($ll,$vv)=parse(substr($bs,$pos,$tt));
		$pos+=$ll;
		$tt-=$ll;
		if($t==0)
		{ #addition
		    $val+=$vv;
		}
		elsif($t==1)
		{
		    $val*=$vv;
		}
		elsif($t==2)
		{
		    if($val > $vv)
		    {
			$val = $vv;
		    }
		}
		elsif($t==3)
		{
		    if($val < $vv)
		    {
			$val = $vv;
		    }
		}
		elsif($t==5)
		{
		    if($val > $vv)
		    {
			$val = 1;
		    }
		    else
		    {
			$val=0;
		    }
		}
		elsif($t==6)
		{
		    if($val < $vv)
		    {
			$val = 1;
		    }
		    else
		    {
			$val=0;
		    }
		}
		elsif($t==7)
		{
		    if($val == $vv)
		    {
			$val = 1;
		    }
		    else
		    {
			$val=0;
		    }
		}
		 
	    }
	}
	else
	{ #number of subpackets
	    $npack=substr($bs,$pos,11);
	    $pos+=11;
	    my $tt=oct("0b$npack");
#	    print "npack: $tt\n";
	    my $ll,$vv;
	    ($ll,$vv)=parse(substr($bs,$pos));
	    $val=$vv;
	    $pos+=$ll;
	    $tt--;
	    while ($tt)
	    {
#		print "ee: $pos $tt $ll\n";
		($ll,$vv)=parse(substr($bs,$pos));
		$tt--;
		$pos+=$ll;
		if($t==0)
		{ #addition
		    $val+=$vv;
		}
		elsif($t==1)
		{
		    $val*=$vv;
		}
		elsif($t==2)
		{
		    if($val > $vv)
		    {
			$val = $vv;
		    }
		}
		elsif($t==3)
		{
		    if($val < $vv)
		    {
			$val = $vv;
		    }
		}
		elsif($t==5)
		{
		    if($val > $vv)
		    {
			$val = 1;
		    }
		    else
		    {
			$val=0;
		    }
		}
		elsif($t==6)
		{
		    if($val < $vv)
		    {
			$val = 1;
		    }
		    else
		    {
			$val=0;
		    }
		}
		elsif($t==7)
		{
		    if($val == $vv)
		    {
			$val = 1;
		    }
		    else
		    {
			$val=0;
		    }
		}

	    }
	}
	return $pos,$val;
    }
}

my $b,$v;
($b,$v) = parse($bs);

print "part1: $vsum\npart2: $v\n";
